from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class Cloud(Base):
  id = Column(Integer, primary_key = True, index = True)
  cloud_type_name = Column(String, nullable = False)
  cloud_type_range_min = Column(Integer, nullable = False)
  cloud_type_range_max = Column(Integer, nullable = False)

  catches = relationship("Catch", back_populates = "clouds")