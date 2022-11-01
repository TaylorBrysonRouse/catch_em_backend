from enum import unique
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class User(Base):
  id = Column(Integer, primary_key = True, index = True)
  username = Column(String, unique = True, nullable = False)
  email = Column(String, unique = True, nullable = False, index = True)
  hashed_password = Column(String, nullable = False)
  is_active = Column(Boolean(), default = True)
  home_lake_id = Column(Integer, ForeignKey("lake.id"))
  
  home_lake = relationship("Lake", back_populates = "locals")
  catches = relationship("Catch", back_populates = "user")