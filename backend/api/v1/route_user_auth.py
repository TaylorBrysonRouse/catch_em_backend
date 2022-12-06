from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta

from db.session import get_db
from core.hashing import PasswordHasher
from schemas.users import UserLogin, UserSignUp
from core.config import settings
from fastapi_jwt_auth import AuthJWT
from db.repository.users import create_user, get_user

# route_login - Endpoint for User Login and Method to Authenticate User
router = APIRouter()

@router.post("/login")
def login(login_data: UserLogin, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
  user = authenticate_user(login_data.username, login_data.password, db)
  if not user: 
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail = "Incorrect username and/or password"
    )
  access_token = Authorize.create_access_token(subject=user.username, expires_time=timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRATION))
  refresh_token = Authorize.create_refresh_token(subject=user.username, expires_time=timedelta(days=settings.JWT_REFRESH_TOKEN_EXPIRATION))
  return {
    "user": {
      "username": user.username, 
      "email": user.email, 
      "is_active": user.is_active 
      }, 
      "access_token": access_token,
      "refresh_token": refresh_token
  }

@router.post("/signup")
def user_signup(user: UserSignUp, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
  user = create_user(user, db)
  if not user:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail = "Sign Up Error"
    )
  access_token = Authorize.create_access_token(subject=user.username, expires_time=timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRATION))
  refresh_token = Authorize.create_refresh_token(subject=user.username, expires_time=timedelta(days=settings.JWT_REFRESH_TOKEN_EXPIRATION))
  return {
    "user": {
      "username": user.username, 
      "email": user.email, 
      "is_active": user.is_active 
      }, 
      "access_token": access_token,
      "refresh_token": refresh_token
  }

@router.post("/refresh")
def refresh_token(Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
  Authorize.jwt_refresh_token_required()

  current_user = get_user(Authorize.get_jwt_subject(), db)
  new_access_token = Authorize.create_access_token(subject=current_user.username)
  return {"access_token": new_access_token}

def authenticate_user(username: str, password: str, db: Session):
  user = get_user(username, db)
  
  if not user:
    return False
  if not PasswordHasher.check_password(password, user.hashed_password):
    return False
  return user