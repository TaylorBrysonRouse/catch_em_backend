from pydantic import BaseModel

# tokens - Schema for tokens
class Token(BaseModel):
  token: str
  token_type: str