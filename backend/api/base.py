from fastapi import APIRouter
from api.v1 import route_users, route_catches, route_login

api_router = APIRouter()
api_router.include_router(route_users.router, prefix = "/users", tags = ["users"])
api_router.include_router(route_catches.router, prefix = "/catches", tags = ["catches"])
api_router.include_router(route_login.router, prefix = "/login", tags = ["login"])