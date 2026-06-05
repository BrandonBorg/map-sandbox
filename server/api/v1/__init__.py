from fastapi import APIRouter
from api.v1.test import test_router
from api.v1.geospatial_file_converter import geospatial_file_converter_router

v1_router = APIRouter()
v1_router.include_router(test_router)
v1_router.include_router(geospatial_file_converter_router)
