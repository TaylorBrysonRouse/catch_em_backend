from sqlalchemy.orm import Session
from db.models.weights import Weight

async def retrieve_weights(db: Session):
  return db.query(Weight).all()