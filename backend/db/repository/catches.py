from sqlalchemy.orm import Session
from schemas.catches import CatchCreate
from db.models.catches import Catch
from db.repository.clouds import get_cloud_type
from db.repository.clarities import find_water_clarity
from core.weather import GetWeatherConditions, GetWindDirection

async def create_catch(catch: CatchCreate, db: Session, user_id: int):
  weather_response = GetWeatherConditions(catch.latitude, catch.longitude, catch.catch_date )

  if "error" in weather_response:
    return weather_response
  else:
    if "rain" in weather_response["main"].lower():
      rain_bool = True
    else:
      rain_bool = False

    catch = Catch(user_id = user_id,
                  latitude = catch.latitude,
                  longitude = catch.longitude,
                  catch_weight = catch.catch_weight,
                  catch_date = catch.catch_date,
                  water_depth = catch.water_depth,
                  water_clarity = find_water_clarity(catch.water_clarity, db),
                  water_temp = catch.water_temp,
                  catch_air_temp = weather_response["temp"],
                  cloud_type_id = get_cloud_type(weather_response["clouds"], db),
                  catch_pressure = weather_response["pressure"],
                  catch_rain = rain_bool,
                  catch_wind_direction = GetWindDirection(weather_response["wind_deg"]),
                  catch_wind_speed = weather_response["wind_speed"],
                  bait_id = catch.bait_id,
                  bait_color_id = catch.bait_color,
                  bait_weight_id = catch.bait_weight
                 )
    db.add(catch)
    db.commit()
    db.refresh(catch)
    return catch

async def retrieve_catch(id: int, db: Session):
  catch = db.query(Catch).filter(Catch.id == id).first()
  return catch

async def retrieve_catches(user_id: int, db: Session):
  catches = db.query(Catch).filter(Catch.user_id == user_id).all()
  return catches