from typing import Optional
from pydantic import BaseModel, EmailStr

class UserSignUp(BaseModel):
  username: str
  email: EmailStr
  password: str
  home_lake_id: int

class ShowUser(BaseModel):
  username: str
  email: EmailStr
  is_active: bool

  class Config():
    orm_mode = True