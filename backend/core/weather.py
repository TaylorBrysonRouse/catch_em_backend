import requests, json

from sqlalchemy.orm import Session

from datetime import datetime, timedelta

from core.config import settings

def GetWeatherConditions(lat, long, time):
  OPEN_WEATHER_MAP_API_KEY = settings.OPEN_WEATHER_MAP_API_KEY
  MINUTES_TO_USE_HISTORY_API = settings.MINUTES_TO_USE_HISTORY_API

  if (datetime.now(time.tzinfo) - timedelta(minutes = int(MINUTES_TO_USE_HISTORY_API)) > time):
    unix_time = datetime(time.year, time.month, time.day, time.hour, time.minute, time.second).timestamp()

    open_weather_map_get_request = f"https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={long}&dt={unix_time}&appid={OPEN_WEATHER_MAP_API_KEY}&units=imperial"
    api_called = 'History'
  else:
    open_weather_map_get_request = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={OPEN_WEATHER_MAP_API_KEY}&units=imperial"
    api_called = 'Current'

  response = requests.get(open_weather_map_get_request).json()

  response["api_called"] = f"{api_called}"

  weather_data = FormatOpenWeatherResponse(response)
  
  return weather_data

def GetWindDirection(wind_deg):
  if wind_deg in range(351, 360) or wind_deg in range(0, 10):
    direction = "North"
  elif wind_deg in range(11, 80):
    direction = "Northeast"
  elif wind_deg in range(81, 100):
    direction = "East"
  elif wind_deg in range(101, 170):
    direction = "Southeast" 
  elif wind_deg in range(171, 190):
    direction = "South"
  elif wind_deg in range(191, 260):
    direction = "Southwest"
  elif wind_deg in range(261, 280):
    direction = "West"
  elif wind_deg in range(281, 350):
    direction = "Northwest"

  return direction

def FormatOpenWeatherResponse(format_response):
  response = json.loads(json.dumps(format_response))

  if response["cod"] == 200:
    if response["api_called"] == 'History':
      weather_data = response["data"]
      data = {
        "main": response['weather'][0]['main'],
        "temp": weather_data['temp'],
        "clouds": weather_data['clouds'],
        "pressure": weather_data['pressure'],
        "wind_deg": weather_data['wind_deg'],
        "wind_speed": weather_data['wind_speed']
      }
    else: # indicies need to be specefied
      data = {
        "main": response['weather'][0]['main'],
        "temp": response['main']['temp'],
        "clouds": response['clouds']['all'],
        "pressure": response['main']['pressure'],
        "wind_deg": response['wind']['deg'],
        "wind_speed": response['wind']['speed']
      }

      return data
  else:
    error = {
      "code": response['cod'],
      "error": response['message']
    }

    return error