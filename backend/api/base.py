from fastapi import APIRouter
from api.v1 import route_users
from api.v1 import routes_catches

api_router = APIRouter()
api_router.include_router(route_users.router, prefix = "/users", tags = ["users"])
api_router.include_router(routes_catches.router, prefix= "/catches", tags = ["catches"])