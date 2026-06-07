from fastapi import APIRouter
from services.geospatial_file_converter_service import *
from services.simple_geometry_service import copy_file_to_table, get_simple_geometry, get_record_count

geospatial_file_converter_router = APIRouter(prefix="/geospatial_file_converter_router", tags=["geospatial_file_converter_router"])

@geospatial_file_converter_router.post("/geojson")
def convert_geojson(file_name: str):
    # create parquet input file
    res = geojson_to_parquet(file_name)
    # save to duckdb
    copy_file_to_table(file_name)
    return {"success":res }

@geospatial_file_converter_router.get("/check_table")
def check_table():
    sample = get_simple_geometry()
    num_records = get_record_count()
    return ({"num_records": num_records, "sample": sample})