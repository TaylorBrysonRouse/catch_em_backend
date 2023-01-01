from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import Depends

from db.session import get_db
from db.repository.weights import retrieve_weights
from db.models.users import User
from core.security import get_current_user

# route_weights - CRUD Endpoints for Weight Model
router = APIRouter()

@router.get('')
async def get_weights(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  weights = await retrieve_weights(db)
  return weights