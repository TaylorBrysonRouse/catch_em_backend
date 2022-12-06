from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi_jwt_auth import AuthJWT

from db.session import get_db
from db.models.users import User
from db.repository.weights import retrieve_weights

# route_weights - CRUD Endpoints for Weight Model
router = APIRouter()

@router.get('')
async def get_weights(db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
  Authorize.jwt_required()
  weights = await retrieve_weights(db)
  return weights