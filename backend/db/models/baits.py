from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

# baits - db model for bait types
class Bait(Base):
  id = Column(Integer, primary_key = True, index = True)
  bait_name = Column(String, nullable = False)

  catches = relationship("Catch", back_populates = "bait_type")