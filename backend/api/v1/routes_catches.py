from venv import create
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status

from db.session import get_db
from db.models.catches import Catch
from schemas.catches import CatchCreate
from db.repository.catches import create_catch

router = APIRouter()

@router.post("/log-catch")
async def log_catch(catch: CatchCreate, db: Session = Depends(get_db)):
  current_user = 1
  catch = await create_catch(catch = catch, db = db, user_id = current_user)
  return catch
