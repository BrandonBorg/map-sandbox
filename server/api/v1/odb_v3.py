from fastapi import APIRouter
from services.geospatial_file_converter_service import *
from services.odb_v3_service import *

odb_v3_router = APIRouter(prefix="/odb_v3", tags=["odb_v3"])

@odb_v3_router.post("/flood_h3_lake")
def flood_h3_lake():
    # create parquet input file
    names = ["ON_1", "ON_2", "ON_3"] # ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "ON_1", "ON_2", "ON_3", "PE", "QC_1", "QC_2", "SK", "YT"]
    for name in names:
        file_name = f"ODB_v3_{name}"
        gpkg_to_parquet(file_name)
        print(f"{file_name} added to data lake")
    return {"success": True }


@odb_v3_router.post("/gpkg")
def convert_gpkg(file_name: str):
    # create parquet input file
    res = gpkg_to_parquet(file_name)
    return {"success":res }
