from fastapi import APIRouter
from services.geospatial_file_converter_service import *
geospatial_file_converter_router = APIRouter(prefix="/geospatial_file_converter_router", tags=["geospatial_file_converter_router"])

@geospatial_file_converter_router.post("/geojson")
def convert_geojson(file_name: str):
    res = geojson_to_parquet(file_name)
    return {"success":res}