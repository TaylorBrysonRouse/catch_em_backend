from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError
import json

from db.session import get_db
from db.repository.users import get_user


from core.config import settings

# security - file that holds actions for access (jwt) tokens
oauth2_access_scheme = OAuth2PasswordBearer(tokenUrl="/login")
oauth2_refresh_scheme = OAuth2PasswordBearer(tokenUrl="/refresh")

def create_access_token(data: dict, expiration: Optional[timedelta] = None):
  to_encode = data.copy()
  if expiration:
    expire = datetime.utcnow() + expiration
  else:
    expire = datetime.utcnow() + timedelta(seconds= settings.JWT_ACCESS_TOKEN_EXPIRATION)
   
  to_encode.update({"exp": expire})

  encoded_jwt = jwt.encode(to_encode, settings.JWT_ACCESS_SECRET, settings.JWT_ALGORITHM)
  return encoded_jwt

def create_refresh_token(data: dict, expiration: Optional[timedelta] = None):
    to_encode = data.copy()
    if expiration:
      expire = datetime.utcnow() + expiration
    else:
      expire = datetime.utcnow() + timedelta(minutes = settings.JWT_REFRESH_TOKEN_EXPIRATION)
      
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, settings.JWT_REFRESH_SECRET, settings.JWT_ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_access_scheme), db: Session = Depends(get_db)):
  authorization_exception = HTTPException(
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Could not verify refresh token"
  )

  try:
    payload = jwt.decode(token, settings.JWT_ACCESS_SECRET, settings.JWT_ALGORITHM)
    username: str = payload.get("username")
    if username is None:
      raise authorization_exception

    user = get_user(username, db)

    if user is None:
      raise authorization_exception

    return user
  except JWTError:
    raise authorization_exception

def verify_refresh_token(token: str = Depends(oauth2_refresh_scheme), db: Session = Depends(get_db)):
  authorization_exception = HTTPException(
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Could not verify refresh token"
  )

  try:
    payload = jwt.decode(token, settings.JWT_REFRESH_SECRET, settings.JWT_ALGORITHM)
    username: str = payload.get("username")
    if username is None:
      raise authorization_exception
      
    user = get_user(username, db)

    if user is None:
      raise authorization_exception

    new_access_token = create_access_token({"username": user.username, "email": user.email})

    return new_access_token
  except JWTError as ex:
    print(ex)
    raise authorization_exception