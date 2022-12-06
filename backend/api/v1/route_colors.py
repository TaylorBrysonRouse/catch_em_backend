from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi_jwt_auth import AuthJWT

from db.session import get_db
from db.repository.colors import retrieve_colors

# route_colors - CRUD Endpoints for Color Model
router = APIRouter()

@router.get('')
async def get_weights(db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
  Authorize.jwt_required()
  colors = await retrieve_colors(db)
  return colors