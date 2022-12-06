from fastapi import APIRouter
from api.v1 import route_user_auth, route_catches, route_baits, route_weights, route_colors

# base - file to include all routes into APIRouter()
api_router = APIRouter()
api_router.include_router(route_catches.router, prefix = "/catches", tags = ["Catches"])
api_router.include_router(route_user_auth.router, prefix = "", tags = ["User Authentication"])
api_router.include_router(route_baits.router, prefix = "/baits", tags = ["Baits"])
api_router.include_router(route_weights.router, prefix = "/weights", tags = ["Weights"])
api_router.include_router(route_colors.router, prefix = "/colors", tags = ["Colors"])