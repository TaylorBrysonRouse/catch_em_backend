from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.orm import relationship

from db.base_class import Base

class Catch(Base):
  id = Column(Integer, primary_key = True, index = True)
  user_id = Column(Integer, ForeignKey("user.id"))
  latitude = Column(DOUBLE_PRECISION, nullable = False)
  longitude = Column(DOUBLE_PRECISION, nullable = False)
