from fastapi import APIRouter
from services.geospatial_file_converter_service import *
from services.odb_v3_service import *

odb_v3_router = APIRouter(prefix="/odb_v3", tags=["odb_v3"])

@odb_v3_router.post("/flood_db")
def flood_db():
    # create parquet input file
    names = ["ON_1", "ON_2", "ON_3"] # ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "ON_1", "ON_2", "ON_3", "PE", "QC_1", "QC_2", "SK", "YT"]
    db = get_db()
    for name in names:
        file_name = f"ODB_v3_{name}"
        gpkg_to_parquet(file_name)
        copy_file_to_odb_v3(file_name, db)
        print(f"{file_name} added to db")
    return {"success": True }


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