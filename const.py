"""Constants for Environment Canada integration."""

from homeassistant.components.weather import (
    ATTR_CONDITION_CLEAR_NIGHT,
    ATTR_CONDITION_CLOUDY,
    ATTR_CONDITION_FOG,
    ATTR_CONDITION_HAIL,
    ATTR_CONDITION_LIGHTNING_RAINY,
    ATTR_CONDITION_PARTLYCLOUDY,
    ATTR_CONDITION_POURING,
    ATTR_CONDITION_RAINY,
    ATTR_CONDITION_SNOWY,
    ATTR_CONDITION_SNOWY_RAINY,
    ATTR_CONDITION_SUNNY,
    ATTR_CONDITION_WINDY
)

from homeassistant.const import (
    ATTR_DEVICE_CLASS,
    ATTR_ICON,
    DEGREE,
    DEVICE_CLASS_HUMIDITY,
    DEVICE_CLASS_PRESSURE,
    DEVICE_CLASS_TEMPERATURE,
    LENGTH_KILOMETERS,
    LENGTH_MILLIMETERS,
    PERCENTAGE,
    SPEED_KILOMETERS_PER_HOUR,
    TEMP_CELSIUS,
    UV_INDEX,
)

DOMAIN = "environment_canada"
ATTRIBUTION = "Data provided by Environment Canada"
ATTR_EN_LABEL = "english"
ATTR_FR_LABEL = "french"
ATTR_UNIT = "unit"

# Icon codes from http://dd.weatheroffice.ec.gc.ca/citypage_weather/
# docs/current_conditions_icon_code_descriptions_e.csv
ICON_CONDITION_MAP = {
    ATTR_CONDITION_SUNNY: [0, 1],
    ATTR_CONDITION_CLEAR_NIGHT: [30, 31],
    ATTR_CONDITION_PARTLYCLOUDY: [2, 3, 4, 5, 22, 32, 33, 34, 35],
    ATTR_CONDITION_CLOUDY: [10],
    ATTR_CONDITION_RAINY: [6, 9, 11, 12, 28, 36],
    ATTR_CONDITION_LIGHTNING_RAINY: [19, 39, 46, 47],
    ATTR_CONDITION_POURING: [13],
    ATTR_CONDITION_SNOWY_RAINY: [7, 14, 15, 27, 37],
    ATTR_CONDITION_SNOWY: [8, 16, 17, 18, 25, 26, 38, 40],
    ATTR_CONDITION_WINDY: [43],
    ATTR_CONDITION_FOG: [20, 21, 23, 24, 44],
    ATTR_CONDITION_HAIL: [26, 27],
}

SENSOR_TYPES = {
    "temperature": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
        ATTR_EN_LABEL: "Temperature",
        ATTR_FR_LABEL: "Température",
        ATTR_UNIT: TEMP_CELSIUS,
        ATTR_ICON: "mdi:thermometer"
    },
    "dewpoint": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
        ATTR_EN_LABEL: "Dew Point",
        ATTR_FR_LABEL: "Point de rosée",
        ATTR_UNIT: TEMP_CELSIUS,
        ATTR_ICON: "mdi:thermometer"
    },
    "wind_chill": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
        ATTR_EN_LABEL: "Wind Chill",
        ATTR_FR_LABEL: "Refroidissement éolien",
        ATTR_UNIT: TEMP_CELSIUS,
        ATTR_ICON: "mdi:thermometer-minus"
    },
    "humidex": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
        ATTR_EN_LABEL: "Humidex",
        ATTR_FR_LABEL: "Humidex",
        ATTR_UNIT: TEMP_CELSIUS,
        ATTR_ICON: "mdi:thermometer-plus"
    },
    "pressure": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_PRESSURE,
        ATTR_EN_LABEL: "Pressure",
        ATTR_FR_LABEL: "Pression",
        ATTR_UNIT: "kPa",
        ATTR_ICON: "mdi:gauge"
    },
    "tendency": {
        ATTR_DEVICE_CLASS: None,
        ATTR_EN_LABEL: "Tendency",
        ATTR_FR_LABEL: "Tendance",
        ATTR_UNIT: None,
        ATTR_ICON: "mdi:swap-vertical"
    },
    "humidity": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_HUMIDITY,
        ATTR_EN_LABEL: "Humidity",
        ATTR_FR_LABEL: "Humidité",
        ATTR_UNIT: PERCENTAGE,
        ATTR_ICON: "mdi:water-percent"
    },
    "visibility": {
        ATTR_DEVICE_CLASS: None,
        ATTR_EN_LABEL: "Visibility",
        ATTR_FR_LABEL: "Visibilité",
        ATTR_UNIT: LENGTH_KILOMETERS,
        ATTR_ICON: "mdi:telescope"
    },
    "condition": {
        ATTR_DEVICE_CLASS: None,
        ATTR_EN_LABEL: "Condition",
        ATTR_FR_LABEL: "Condition",
        ATTR_UNIT: None,
        ATTR_ICON: "mdi:weather-partly-snowy-rainy"
    },
    "text_summary": {
        ATTR_DEVICE_CLASS: None,
        ATTR_EN_LABEL: "Forecast",
        ATTR_FR_LABEL: "Prévision",
        ATTR_UNIT: None,
        ATTR_ICON: "mdi:weather-partly-snowy-rainy"
    },
    "wind_speed": {
        ATTR_DEVICE_CLASS: None,
        ATTR_EN_LABEL: "Wind Speed",
        ATTR_FR_LABEL: "Vitesse de vent",
        ATTR_UNIT: SPEED_KILOMETERS_PER_HOUR,
        ATTR_ICON: "mdi:weather-windy"
    },
    "wind_gust": {
        ATTR_DEVICE_CLASS: None,
        ATTR_EN_LABEL: "Wind Gust",
        ATTR_FR_LABEL: "Rafale de vent",
        ATTR_UNIT: SPEED_KILOMETERS_PER_HOUR,
        ATTR_ICON: "mdi:weather-windy"
    },
    "wind_dir": {
        ATTR_DEVICE_CLASS: None,
        ATTR_EN_LABEL: "Wind Direction",
        ATTR_FR_LABEL: "Direction de vent",
        ATTR_UNIT: None,
        ATTR_ICON: "mdi:sign-direction"
    },
    "wind_bearing": {
        ATTR_DEVICE_CLASS: None,
        ATTR_EN_LABEL: "Wind Bearing",
        ATTR_FR_LABEL: "Palier de vent",
        ATTR_UNIT: DEGREE,
        ATTR_ICON: "mdi:sign-direction"
    },
    "high_temp": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
        ATTR_EN_LABEL: "High Temperature",
        ATTR_FR_LABEL: "Haute température",
        ATTR_UNIT: TEMP_CELSIUS,
        ATTR_ICON: "mdi:thermometer-chevron-up"
    },
    "low_temp": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
        ATTR_EN_LABEL: "Low Temperature",
        ATTR_FR_LABEL: "Basse température",
        ATTR_UNIT: TEMP_CELSIUS,
        ATTR_ICON: "mdi:thermometer-chevron-down"
    },
    "uv_index": {
        ATTR_DEVICE_CLASS: None,
        ATTR_EN_LABEL: "UV Index",
        ATTR_FR_LABEL: "Indice UV",
        ATTR_UNIT: UV_INDEX,
        ATTR_ICON: "mdi:weather-sunny-alert"
    },
    "pop": {
        ATTR_DEVICE_CLASS: None,
        ATTR_EN_LABEL: "Chance of Precip.",
        ATTR_FR_LABEL: "Probabilité d'averses",
        ATTR_UNIT: PERCENTAGE,
        ATTR_ICON: "mdi:weather-snowy-rainy"
    },
    "icon_code": {
        ATTR_DEVICE_CLASS: None,
        ATTR_EN_LABEL: "Icon Code",
        ATTR_FR_LABEL: "Code icône",
        ATTR_UNIT: None,
        ATTR_ICON: "mdi:weather-partly-snowy-rainy"
    },
    "precip_yesterday": {
        ATTR_DEVICE_CLASS: None,
        ATTR_EN_LABEL: "Precipitation Yesterday",
        ATTR_FR_LABEL: "Précipitation d'hier",
        ATTR_UNIT: LENGTH_MILLIMETERS,
        ATTR_ICON: "mdi:weather-snowy-rainy"
    },
    "warnings": {
        ATTR_DEVICE_CLASS: None,
        ATTR_EN_LABEL: "Warnings",
        ATTR_FR_LABEL: "Alertes",
        ATTR_UNIT: None,
        ATTR_ICON: "mdi:alert-octagon"
    },
    "watches": {
        ATTR_DEVICE_CLASS: None,
        ATTR_EN_LABEL: "Watches",
        ATTR_FR_LABEL: "Veilles",
        ATTR_UNIT: None,
        ATTR_ICON: "mdi:alert"
    },
    "advisories": {
        ATTR_DEVICE_CLASS: None,
        ATTR_EN_LABEL: "Advisories",
        ATTR_FR_LABEL: "Avis",
        ATTR_UNIT: None,
        ATTR_ICON: "mdi:bell-alert"
    },
    "statements": {
        ATTR_DEVICE_CLASS: None,
        ATTR_EN_LABEL: "Statements",
        ATTR_FR_LABEL: "Bulletins",
        ATTR_UNIT: None,
        ATTR_ICON: "mdi:bell-alert"
    },
    "endings": {
        ATTR_DEVICE_CLASS: None,
        ATTR_EN_LABEL: "Endings",
        ATTR_FR_LABEL: "Terminaisons",
        ATTR_UNIT: None,
        ATTR_ICON: "mdi:alert-circle-check"
    },
}
