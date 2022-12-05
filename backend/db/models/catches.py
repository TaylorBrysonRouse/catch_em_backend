from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.orm import relationship

from db.base_class import Base

# catches - db model for catches
class Catch(Base):
  id = Column(Integer, primary_key = True, index = True)
  user_id = Column(Integer, ForeignKey("user.id"), nullable = False)
  latitude = Column(DOUBLE_PRECISION, nullable = False)
  longitude = Column(DOUBLE_PRECISION, nullable = False)
  catch_weight = Column(DOUBLE_PRECISION, nullable = True)
  catch_date = Column(DateTime, nullable = False)
  water_depth = Column(DOUBLE_PRECISION, nullable = True)
  water_clarity_id = Column(Integer, ForeignKey("clarity.id"), nullable = True)
  water_temp = Column(DOUBLE_PRECISION, nullable = True)
  catch_air_temp = Column(DOUBLE_PRECISION, nullable = False)
  cloud_type_id = Column(Integer, ForeignKey("cloud.id"))
  catch_pressure = Column(DOUBLE_PRECISION, nullable = False)
  catch_rain = Column(Boolean, nullable = False)
  catch_wind_direction = Column(String, nullable = False)
  catch_wind_speed = Column(Integer, nullable = False)
  bait_id = Column(Integer, ForeignKey("bait.id"), nullable = True)
  bait_color_id = Column(Integer, ForeignKey("color.id"), nullable = True)
  bait_weight_id = Column(Integer, ForeignKey("weight.id"), nullable = True)

  user = relationship("User", back_populates = "catches")
  water_clarity = relationship("Clarity", back_populates = "catches")
  clouds = relationship("Cloud", back_populates = "catches")
  bait_type = relationship("Bait", back_populates = "catches")
  bait_color = relationship("Color", back_populates = "catches")
  bait_weight = relationship("Weight", back_populates = "catches")

