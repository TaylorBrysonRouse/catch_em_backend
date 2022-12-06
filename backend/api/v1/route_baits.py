from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi_jwt_auth import AuthJWT

from db.session import get_db
from db.models.users import User
from db.repository.bait_types import retrieve_bait_types

# route_baits - CRUD Endpoints for Baits Model
router = APIRouter()

@router.get('')
async def get_bait_types(db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
  Authorize.jwt_required()
  baits = await retrieve_bait_types(db)
  return baits
