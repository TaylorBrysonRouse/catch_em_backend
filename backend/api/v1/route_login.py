from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta

from db.session import get_db
from core.hashing import PasswordHasher
from schemas.tokens import Token
from db.repository.login import get_user
from core.security import create_access_token
from core.config import settings
from jose import JWTError, jwt

# route_login - Endpoint for User Login and Method to Authenticate User
router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")

@router.post("/token")
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
  return {"user": {"username": user.username, "email": user.email, "is_active": user.is_active }, "access_token": access_token}


def authenticate_user(username: str, password: str, db: Session):
  user = get_user(username = username, db = db)
  
  if not user:
    return False
  if not PasswordHasher.check_password(password, user.hashed_password):
    return False
  return user

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
  authorization_exception = HTTPException(
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Could not authorize user"
  )
  try: 
    payload = jwt.decode(token, settings.JWT_SECRET, algorithms = [settings.JWT_ALGORITHM])
    username: str = payload.get("username")
    
    if username is None:
      raise authorization_exception
  except JWTError:
    raise authorization_exception
  user = get_user(username = username, db = db)
  if user is None:
    raise authorization_exception
  return user