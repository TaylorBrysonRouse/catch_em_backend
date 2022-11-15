from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import Depends

from db.session import get_db
from api.v1.route_login import get_current_user
from db.models.users import User
from db.repository.colors import retrieve_colors

router = APIRouter()

@router.get('/')
async def get_weights(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  colors = await retrieve_colors(db = db)
  return colors