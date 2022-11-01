import requests, json, datetime

from core.config import settings

OPEN_WEATHER_MAP_API_KEY = settings.OPEN_WEATHER_MAP_API_KEY

OPEN_WEATHER_MAP_URL = "https://history.openweathermap.org/data/3.0/history/timemachine?"

def get_weather_conditions(lat, long, time):
  unix_time = datetime.datetime(time.year, time.month, time.day, time.hour, time.minute, time.secound).timestamp()

  open_weather_map_get_request = f"{OPEN_WEATHER_MAP_URL}lat={lat}&long={long}&dt={unix_time}&appid={OPEN_WEATHER_MAP_API_KEY}"

  response = requests.get(open_weather_map_get_request).json()

  return response