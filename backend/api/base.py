from fastapi import APIRouter
from api.v1 import route_users, route_catches, route_login, route_baits, route_weights, route_colors

# base - file to include all routes into APIRouter()
api_router = APIRouter()
api_router.include_router(route_users.router, prefix = "/users", tags = ["users"])
api_router.include_router(route_catches.router, prefix = "/catches", tags = ["catches"])
api_router.include_router(route_login.router, prefix = "/login", tags = ["login"])
api_router.include_router(route_baits.router, prefix = "/baits", tags = ["baits"])
api_router.include_router(route_weights.router, prefix = "/weights", tags = ["weights"])
api_router.include_router(route_colors.router, prefix = "/colors", tags = ["colors"])