Home Assistant Custom Component  
Environment Canada
===

## Installation

Place the files from this repository in the `custom_components` folder of your Home Assistant installation, in a folder named `environment_canada`. For example, run the following commands in the `custom_components` folder:

```
git clone https://github.com/michaeldavie/hass_environment_canada.git
mv hass_environment_canada environment_canada
```

## Simple Configuration

```yaml
weather:
  - platform: environment_canada

sensor:
  - platform: environment_canada

camera:
  - platform: environment_canada
```

---

## Detailed Configuration

### Weather

Use the station closest to Home Assistant's configured location:

```yaml
weather:
  - platform: environment_canada
```

Use the station closest to a specific location:

```yaml
weather:
  - platform: environment_canada
    latitude: 50
    longitude: -100
```

Use a specifc station from [this list](https://dd.weather.gc.ca/citypage_weather/docs/site_list_en.csv):

```yaml
weather:
  - platform: environment_canada
    station: MB/s0000492
```

Use hourly forecasts instead of daily:

```yaml
weather:
  - platform: environment_canada
    forecast: hourly
```

---

### Sensors

Use the station closest to Home Assistant's configured location:

```yaml
sensor:
  - platform: environment_canada
```

Use the station closest to a specific location:

```yaml
sensor:
  - platform: environment_canada
    latitude: 50
    longitude: -100
```

Use a specifc station from [this list](https://dd.weather.gc.ca/citypage_weather/docs/site_list_en.csv):

```yaml
sensor:
  - platform: environment_canada
    station: MB/s0000492
```

---

### Camera (Radar Map)

Centred on Home Assistant's configured location:

```yaml
camera:
  - platform: environment_canada
```

Centred on a specific location:

```yaml
camera:
  - platform: environment_canada
    latitude: 50
    longitude: -100
```

Use a static image instead of a loop:

```yaml
camera:
  - platform: environment_canada
    loop: false
```

Use rain display:

```yaml
camera:
  - platform: environment_canada
    precip_type: rain
```

Use snow display:

```yaml
camera:
  - platform: environment_canada
    precip_type: snow
```
