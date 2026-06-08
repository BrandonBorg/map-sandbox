from fastapi import APIRouter
from services.geospatial_file_converter_service import *
from services.odb_v3_service import *

odb_v3_router = APIRouter(prefix="/odb_v3", tags=["odb_v3"])

@odb_v3_router.post("/gpkg")
def convert_gpkg(file_name: str):
    # create parquet input file
    res = gpkg_to_parquet(file_name)
    # save to duckdb
    copy_file_to_odb_v3(file_name)
    return {"success":res }

@odb_v3_router.get("/feature_count")
def feature_count():
    # create parquet input file
    feature_count = get_record_count()
    features_100 = get()
    return {"feature_count":feature_count, "features_100":features_100}

# change to delete source??? or provience?
@odb_v3_router.delete("/table")
def delete_table():
    # create parquet input file
    clear_table()
    return {"res":True}