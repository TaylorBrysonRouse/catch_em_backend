from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError

from core.config import settings

# security - file that holds actions for access (jwt) tokens
def create_access_token(data: dict, expiration: Optional[timedelta] = None):
  to_encode = data.copy()
  if expiration:
    expire = datetime.utcnow() + expiration
  else:
    expire = datetime.utcnow() + timedelta(minutes = settings.JWT_TOKEN_EXPIRATION_MINUTES)
   
  to_encode.update({"exp": expire})

  encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm = settings.JWT_ALGORITHM)
  return encoded_jwt