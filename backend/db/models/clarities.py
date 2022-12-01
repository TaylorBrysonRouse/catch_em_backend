from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

# clairties - db model for water clarity types
class Clarity(Base):
  id = Column(Integer, primary_key = True, index = True)
  water_clarity_name = Column(String, nullable = False)
  water_clarity_range = Column(String, nullable = False)
  
  catches = relationship("Catch", back_populates = "water_clarity")