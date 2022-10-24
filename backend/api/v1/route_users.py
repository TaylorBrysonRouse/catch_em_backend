from ssl import cert_time_to_seconds
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.users import ShowUser, UserSignUp
from db.session import get_db
from db.repository.users import create_user

router = APIRouter()

@router.post("/signup", response_model = ShowUser)
def create_user(user: UserSignUp, db: Session = Depends(get_db))
  user = create_user(user = user, db = db)
  return user