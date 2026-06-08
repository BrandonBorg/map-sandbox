from fastapi import APIRouter
from services.geospatial_file_converter_service import *

odb_v3_router = APIRouter(prefix="/odb_v3", tags=["odb_v3"])

@odb_v3_router.post("/gpkg")
def convert_gpkg(file_name: str):
    # create parquet input file
    res = gpkg_to_parquet(file_name)
    # save to duckdb
    #copy_file_to_table(file_name)
    return {"success":res }