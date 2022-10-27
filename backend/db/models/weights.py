from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class Weight(Base):
  id = Column(Integer, primary_key = True, index = True)
  weight_name = Column(String, nullable = False)

  catches = relationship("Catch", back_populates = "bait_weight")