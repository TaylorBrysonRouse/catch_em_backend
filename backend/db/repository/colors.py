from sqlalchemy.orm import Session
from db.models.colors import Color

async def retrieve_colors(db: Session):
  return db.query(Color).all()

def find_color(color_name: str, db: Session):
  return db.query(Color).filter(Color.color_name == color_name).first()
