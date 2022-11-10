from venv import create
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status

from typing import List

from db.session import get_db
from db.models.catches import Catch
from schemas.catches import CatchCreate
from db.repository.catches import create_catch, retrieve_catch, retrieve_catches

router = APIRouter()

@router.post("/log-catch")
async def log_catch(catch: CatchCreate, db: Session = Depends(get_db)):
  current_user = 1
  catch = await create_catch(catch = catch, db = db, user_id = current_user)
  return catch

@router.get("/catches/{id}")
async def get_catch(id: int, db: Session = Depends(get_db)):
  catch = await retrieve_catch(id = id, db = db)
  return catch

@router.get("/catches")
async def get_catches(db: Session = Depends(get_db)):
  user_id = 1
  catches = await retrieve_catches(user_id = user_id, db = db)
  return catches
