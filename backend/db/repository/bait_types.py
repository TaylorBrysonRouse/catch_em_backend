from sqlalchemy.orm import Session
from db.models.baits import Bait

async def retrieve_bait_types(db: Session):
  return db.query(Bait).all()

def find_bait_type(bait_name: str, db: Session):
  return db.query(Bait).filter(Bait.bait_name == bait_name).first()