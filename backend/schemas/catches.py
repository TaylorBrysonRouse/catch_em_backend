from typing import Optional
from pydantic import BaseModel, EmailStr

class UserSignUp(BaseModel):
  username: str
  email: EmailStr
  password: str