import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
  PROJECT_NAME: str = "Catch 'Em"
  PROJECT_VERSION: str = "1.0.0"

  POSTGRES_USER : str = os.getenv("POSTGRES_USER")
  POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
  POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
  POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432
  POSTGRES_TEST_DB: str = os.getenv("POSTGRES_TEST_DB","tdd")
  POSTGRES_DB : str = os.getenv("POSTGRES_DB","tdd")

  DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

  TEST_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_TEST_DB}"

  OPEN_WEATHER_MAP_API_KEY = os.getenv("OPEN_WEATHER_MAP_API_KEY")
  MINUTES_TO_USE_HISTORY_API = os.getenv("MINUTES_TO_USE_HISTORY_API")
settings = Settings()