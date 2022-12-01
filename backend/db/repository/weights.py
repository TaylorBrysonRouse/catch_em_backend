from sqlalchemy.orm import Session
from db.models.weights import Weight

# weights - file used for handling weight methods that touch the db
async def retrieve_weights(db: Session):
  return db.query(Weight).all()

def find_weight(weight_name: str, db: Session):
  return db.query(Weight).filter(Weight.weight_name == weight_name).first()