from xmlrpc.client import DateTime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.orm import relationship

from db.base_class import Base

class Catch(Base):
  id = Column(Integer, primary_key = True, index = True)
  user_id = Column(Integer, ForeignKey("user.id"), nullable = False)
  latitude = Column(DOUBLE_PRECISION, nullable = False)
  longitude = Column(DOUBLE_PRECISION, nullable = False)
  catch_weight = Column(DOUBLE_PRECISION, nullable = True)
  catch_date = Column(DateTime, nullable = False)
  water_depth = Column(DOUBLE_PRECISION, nullable = True)
  water_clarity_id = Column(Integer, ForeignKey("water_clarity.id"), nullable = True)
  water_temp = Column(DOUBLE_PRECISION, nullable = True)
  catch_air_temp = Column(DOUBLE_PRECISION, nullable = False)
  catch_cloud_id = Column(Integer, ForeignKey("cloud_type.id"))
  catch_pressure = Column(DOUBLE_PRECISION, nullable = False)
  catch_rain = Column(Boolean, nullable = False)
  catch_wind_direction = Column(String, nullable = False)
  catch_wind_speed = Column(Integer, nullable = False)
  bait_id = Column(Integer, ForeignKey("baits.id"), nullable = True)
  bait_color_id = Column(Integer, ForeignKey("color.id"), nullable = True)
  bait_weight_id = Column(Integer, ForeignKey("weight.id"), nullable = True)

  user = relationship("User", back_populates = "catches")
  water_clarity = relationship("WaterClarity", back_populates = "catches")
  cloud_coverage = relationship("CloudType", back_populates = "catches")
  bait_type = relationship("Bait", back_populates = "catches")
  bait_color = relationship("Color", back_populates = "catches")
  bait_weight = relationship("Weight", back_populates = "catches")

