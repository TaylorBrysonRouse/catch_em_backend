from optparse import Option
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class CatchCreate(BaseModel):
  latitude: float
  longitude: float
  catch_weight: Optional[float] = None
  catch_date: datetime
  water_depth: Optional[float] = None
  water_clarity: Optional[str] = None
  water_temp: Optional[float] = None
  bait_id: Optional[int] = None
  bait_color: Optional[int] = None
  bait_weight: Optional[int] = None