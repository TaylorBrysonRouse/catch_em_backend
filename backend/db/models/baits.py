from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class Bait(Base):
  id = Column(Integer, primary_key = True, index = True)
  bait_name = Column(String, nullable = False)