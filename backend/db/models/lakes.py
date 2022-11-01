from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.orm import relationship

from db.base_class import Base

class Lake(Base):
  id = Column(Integer, primary_key = True, index = True)
  lake_name = Column(String, unique = True, nullable = False)
  lake_state = Column(String, nullable = False)
  lake_latitude = Column(DOUBLE_PRECISION, nullable = False)
  lake_longitude = Column(DOUBLE_PRECISION, nullable = False)
  locals = relationship("User", back_populates="home_lake")