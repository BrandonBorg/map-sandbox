from fastapi import APIRouter
from api.v1.load_router import load_router
from api.v1.tiles_router import tiles_router
from api.v1.debug_router import debug_router

v1_router = APIRouter()
v1_router.include_router(load_router)
v1_router.include_router(tiles_router)
v1_router.include_router(debug_router)

