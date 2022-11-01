from sqlalchemy.orm import Session
from schemas.users import UserSignUp
from db.models.users import User
from core.hashing import PasswordHasher

def create_user(user: UserSignUp, db: Session):
  user = User(username = user.username,
              email = user.email,
              hashed_password = PasswordHasher.get_password_hash(user.password),
              is_active = True,
              )
  db.add(user)
  db.commit()
  db.refresh(user)
  return user
