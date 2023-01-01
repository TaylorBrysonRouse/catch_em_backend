from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db
from core.hashing import PasswordHasher
from schemas.users import UserLogin, UserSignUp
from db.repository.users import create_user, get_user
from core.security import create_access_token, create_refresh_token, verify_refresh_token

# route_login - Endpoint for User Login and Method to Authenticate User
router = APIRouter()

@router.post("/login")
def login(login_data: UserLogin, db: Session = Depends(get_db)):
  user = authenticate_user(login_data.username, login_data.password, db)
  if not user: 
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail = "Incorrect username and/or password"
    )

  access_token = create_access_token({"username": user.username, "email": user.email})
  refresh_token = create_refresh_token(data = {"username": user.username, "email": user.email})

  return {
    "id": user.id,
    "username": user.username, 
    "email": user.email, 
    "is_active": user.is_active,  
    "access_token": access_token,
    "refresh_token": refresh_token
  }

@router.post("/signup")
def user_signup(user: UserSignUp, db: Session = Depends(get_db)):
  user = create_user(user, db)
  if not user:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail = "Sign Up Error"
    )

  access_token = create_access_token({"username": user.username, "email": user.email})
  refresh_token = create_refresh_token(data = {"username": user.username, "email": user.email}) 
  
  return {
    "id": user.id,
    "username": user.username, 
    "email": user.email, 
    "is_active": user.is_active,  
    "access_token": access_token,
    "refresh_token": refresh_token
  }

@router.post("/refresh")
def refresh_token(verify_refresh_token: str = Depends(verify_refresh_token), db: Session = Depends(get_db)):
  new_access_token = verify_refresh_token

  return {"access_token": new_access_token}

def authenticate_user(username: str, password: str, db: Session):
  user = get_user(username, db)
  
  if not user:
    return False
  if not PasswordHasher.check_password(password, user.hashed_password):
    return False
  return user