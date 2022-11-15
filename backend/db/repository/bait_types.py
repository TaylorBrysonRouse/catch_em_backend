from sqlalchemy.orm import Session
from db.models.baits import Bait

async def retrieve_bait_types(db: Session):
  return db.query(Bait).all()