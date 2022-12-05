from typing import Any
from typing import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#this is to include backend dir in sys.path so that we can import from db,main.py

from db.base import Base
from db.session import SQLALCHEMY_DATABASE_URL, get_db
from api.base import api_router
from core.config import settings

# conftest - Automated Test Config File
def start_application():
  app = FastAPI()
  app.include_router(api_router)
  return app

SQLALCHEMY_DATABASE_URL = settings.TEST_DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionTesting = sessionmaker(autocommit = False, autoflush = False, bind = engine)

@pytest.fixture(scope = "function")
def app() -> Generator[FastAPI, Any, None]:
  """
  Create a fresh DB for each test.
  """
  Base.metadata.create_all(engine)
  _app = start_application()
  yield _app
  Base.metadata.drop_all(engine)

@pytest.fixture(scope = "function")
def db_session(app: FastAPI) -> Generator[SessionTesting, Any, None]:
  connection = engine.connect()
  transaction = connection.begin()
  session = SessionTesting(bind = connection)
  yield session
  session.close()
  transaction.rollback()
  connection.close()

@pytest.fixture(scope = "function")
def client(app: FastAPI, db_session: SessionTesting) -> Generator[TestClient, Any, None]:
  """
  Create new FastAPI TestClient that uses `db_session` fixture to overide
  the `get_db` dependency that is injected into routes
  """

  def _get_test_db():
    try:
      yield db_session
    finally:
      pass
  
  app.dependency_overrides[get_db] = _get_test_db
  with TestClient(app) as client:
    yield client