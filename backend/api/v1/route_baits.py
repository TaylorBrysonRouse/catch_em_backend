from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi import Depends

from db.session import get_db
from api.v1.route_login import get_current_user
from db.models.users import User
from db.repository.bait_types import retrieve_bait_types

router = APIRouter()

@router.get('/')
async def get_bait_types(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  baits = await retrieve_bait_types(db = db)
  return baits
