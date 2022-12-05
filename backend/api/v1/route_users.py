from fastapi import APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.users import ShowUser, UserSignUp
from db.session import get_db
from db.repository.users import create_user
from core.security import create_access_token

# route_users - Endpoint for User Signup
router = APIRouter()

@router.post("/signup")
def user_signup(user: UserSignUp, db: Session = Depends(get_db)): #start here
  user = create_user(user = user, db = db)
  if not user:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail = "Sign Up Error"
    )
  access_token = create_access_token(
    data = {"username": user.username, "email": user.email}
  )
  return {"user": {"username": user.username, "email": user.email, "is_active": user.is_active }, "access_token": access_token}
