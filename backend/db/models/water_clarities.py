from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class WaterClarity(Base):
  #fill in other columns
  
  catches = relationship("Catch", back_populates = "water_clarity")