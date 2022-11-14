from venv import create
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status

from typing import List

from db.session import get_db
from db.models.catches import Catch
from db.models.users import User
from schemas.catches import CatchCreate
from db.repository.catches import create_catch, retrieve_catch, retrieve_catches
from api.v1.route_login import get_current_user

router = APIRouter()

@router.post("/log-catch")
async def log_catch(catch: CatchCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  catch = await create_catch(catch = catch, db = db, user_id = current_user.id)
  return catch

@router.get("/{id}")
async def get_catch(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  catch = await retrieve_catch(id = id, db = db)
  if not catch:
    return HTTPException(
      status_code = status.HTTP_404_NOT_FOUND,
      detail = f"Catch #{id} cannot be found"
      )
  if catch.id == current_user.id:
    return catch
  else:
    return HTTPException(
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = f"User not permitted to access Catch #{id}"
  )

@router.get("/")
async def get_catches(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  catches = await retrieve_catches(user_id = current_user.id, db = db)
  return catches
