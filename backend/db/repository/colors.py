from sqlalchemy.orm import Session
from db.models.colors import Color

async def retrieve_colors(db: Session):
  return db.query(Color).all()