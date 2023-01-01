import os
from dotenv import load_dotenv
from pydantic import BaseSettings

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# config - File used for accessing environment variables
class Settings(BaseSettings):
  PROJECT_NAME: str = "Catch 'Em"
  PROJECT_VERSION: str = "1.0.0"

  POSTGRES_USER : str = os.getenv("POSTGRES_USER")
  POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
  POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
  POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432
  POSTGRES_TEST_DB: str = os.getenv("POSTGRES_TEST_DB","tdd")
  POSTGRES_DB : str = os.getenv("POSTGRES_DB","ddd")

  DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

  TEST_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_TEST_DB}"

  JWT_ACCESS_SECRET: str = os.getenv("JWT_ACCESS_SECRET")
  JWT_REFRESH_SECRET: str = os.getenv("JWT_REFRESH_SECRET")
  JWT_ACCESS_TOKEN_EXPIRATION: int = os.getenv("JWT_ACCESS_TOKEN_EXPIRATION")
  JWT_REFRESH_TOKEN_EXPIRATION: int = os.getenv("JWT_REFRESH_TOKEN_EXPIRATION")
  JWT_ALGORITHM = "HS256"

  OPEN_WEATHER_MAP_API_KEY = os.getenv("OPEN_WEATHER_MAP_API_KEY")
  MINUTES_TO_USE_HISTORY_API = os.getenv("MINUTES_TO_USE_HISTORY_API")

settings = Settings()