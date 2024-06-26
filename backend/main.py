from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from core.config import settings
from api.base import api_router
from db.session import engine
from db.base import Base

# main - Entry Point for Catch 'Em Backend API
def include_router(app):
  app.include_router(api_router)

def create_tables():
  Base.metadata.create_all(bind=engine)

def start_application():
  app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
  create_tables()
  include_router(app)
  return app

app = start_application()