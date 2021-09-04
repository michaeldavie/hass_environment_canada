"""Support for the Environment Canada weather service."""
from datetime import datetime, timedelta
import logging
import re

import async_timeout
from env_canada import ECWeather  # pylint: disable=import-error
import voluptuous as vol

from homeassistant.components.sensor import PLATFORM_SCHEMA, SensorEntity
from homeassistant.const import (
    ATTR_ATTRIBUTION,
    ATTR_LOCATION,
    ATTR_TIME,
    CONF_LATITUDE,
    CONF_LONGITUDE,
)
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

from .const import (
    ATTRIBUTION,
    ATTR_ICON,
    ATTR_UNIT,
    SENSOR_TYPES
)

_LOGGER = logging.getLogger(__name__)

ATTR_UPDATED = "updated"
ATTR_STATION = "station"

CONF_STATION = "station"
CONF_LANGUAGE = "language"


def validate_station(station):
    """Check that the station ID is well-formed."""
    if station is None:
        return
    if not re.fullmatch(r"[A-Z]{2}/s0000\d{3}", station):
        raise vol.error.Invalid('Station ID must be of the form "XX/s0000###"')
    return station


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_LANGUAGE, default="english"): vol.In(["english", "french"]),
        vol.Optional(CONF_STATION): validate_station,
        vol.Inclusive(CONF_LATITUDE, "latlon"): cv.latitude,
        vol.Inclusive(CONF_LONGITUDE, "latlon"): cv.longitude,
    }
)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Environment Canada sensor."""

    if config.get(CONF_STATION):
        ec_data = ECWeather(
            station_id=config[CONF_STATION], language=config.get(CONF_LANGUAGE)
        )
    else:
        lat = config.get(CONF_LATITUDE, hass.config.latitude)
        lon = config.get(CONF_LONGITUDE, hass.config.longitude)
        ec_data = ECWeather(coordinates=(lat, lon), language=config.get(CONF_LANGUAGE))

    async def async_update_data():
        """Fetch data from Environment Canada."""
        async with async_timeout.timeout(10):
            await ec_data.update()
        ec_data.conditions.update(ec_data.alerts)
        return ec_data.conditions

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name="environment_canada_sensor",
        update_method=async_update_data,
        update_interval=timedelta(minutes=5),
    )

    # Fetch initial data so we have data when entities subscribe
    await coordinator.async_refresh()

    async_add_entities(
        ECSensor(coordinator, sensor_type, ec_data.language, ec_data.metadata)
        for sensor_type in coordinator.data
    )


class ECSensor(CoordinatorEntity):
    """Implementation of an Environment Canada sensor."""

    def __init__(self, coordinator, sensor_type, language, metadata):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.sensor_type = sensor_type
        self.language = language
        self.metadata = metadata

    @property
    def unique_id(self) -> str:
        """Return the unique ID of the sensor."""
        return f"{self.metadata['location']}-{self.sensor_type}"

    @property
    def name(self):
        """Return the name of the sensor."""
        return SENSOR_TYPES[self.sensor_type][self.language]

    @property
    def icon(self):
        """Return the icon."""
        return SENSOR_TYPES[self.sensor_type][ATTR_ICON]

    @property
    def state(self):
        """Return the state of the sensor."""
        value = self.coordinator.data[self.sensor_type].get("value")

        if isinstance(value, list):
            return " | ".join([str(s.get("title")) for s in value])[:255]
        if self.sensor_type == "tendency":
            return str(value).capitalize()
        if value is not None and len(str(value)) > 255:
            _LOGGER.info("Value for %s truncated to 255 characters", self.unique_id)
            return str(value)[:255]
        return str(value)

    @property
    def unit_of_measurement(self):
        """Return the units of measurement."""
        return SENSOR_TYPES[self.sensor_type][ATTR_UNIT]

    async def async_update(self):
        """Update current conditions."""
        await self.ec_data.update()

        self.ec_data.conditions.update(self.ec_data.alerts)

    @property
    def device_state_attributes(self):
        """Return the state attributes of the device."""
        attributes = {
            ATTR_ATTRIBUTION: ATTRIBUTION,
            ATTR_LOCATION: self.metadata.get("location"),
            ATTR_STATION: self.metadata.get("station"),
        }

        timestamp = self.metadata.get("timestamp")
        if timestamp:
            attributes[ATTR_UPDATED] = timestamp.isoformat()
        else:
            attributes[ATTR_UPDATED] = None

        value = self.coordinator.data[self.sensor_type].get("value")
        if isinstance(value, list):
            attributes[ATTR_TIME] = " | ".join([str(s.get("date")) for s in value])

        return attributes
