from sqlalchemy.orm import Session
from db.models.clarities import Clarity

# clarities - file used for handling water clarity methods that touch the db
def find_water_clarity(water_clarity, db: Session):
  return db.query(Clarity).filter_by(water_clarity_name = water_clarity).first()
