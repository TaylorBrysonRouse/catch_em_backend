from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from core.config import settings
from api.base import api_router
from db.session import engine
from db.base import Base
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException

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

@AuthJWT.load_config
def get_config():
  return settings

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )