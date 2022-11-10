from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta

from db.session import get_db
from core.hashing import PasswordHasher
from schemas.tokens import Token
from db.repository.login import get_user
from core.security import create_access_token
from core.config import settings

router = APIRouter()

@router.post("/token", response_model = Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
  user = authenticate_user(form_data.username, form_data.password, db)
  if not user: 
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail = "Incorrect username and/or password"
    )
  access_token = create_access_token(
    data = {"username": user.username, "email": user.email}
  )
  return {"token": access_token, "token_type": "bearer"}


def authenticate_user(username: str, password: str, db: Session):
  user = get_user(username = username, db = db)
  
  if not user:
    return False
  if not PasswordHasher.check_password(password, user.hashed_password):
    return False
  return user


