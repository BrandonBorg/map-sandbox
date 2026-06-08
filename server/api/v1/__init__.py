from fastapi import APIRouter
from api.v1.odb_v3 import odb_v3_router
from api.v1.tiles import tiles_router
from api.v1.simple_geometry import simple_geometry_router

v1_router = APIRouter()
v1_router.include_router(simple_geometry_router)
v1_router.include_router(odb_v3_router)

v1_router.include_router(tiles_router)

