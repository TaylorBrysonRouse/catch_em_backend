from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

# colors - db model for colors
class Color(Base):
  id = Column(Integer, primary_key = True, index = True)
  color_name = Column(String, nullable = False)

  catches = relationship("Catch", back_populates = "bait_color")