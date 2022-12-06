from typing import Optional
from pydantic import BaseModel, EmailStr

# users - schema for user signup and showing a user
class UserSignUp(BaseModel):
  username: str
  email: EmailStr
  password: str

class ShowUser(BaseModel):
  username: str
  email: EmailStr
  is_active: bool

  class Config():
    orm_mode = True

class UserLogin(BaseModel):
  username: str
  password: str