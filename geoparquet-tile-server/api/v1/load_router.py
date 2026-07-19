from fastapi import APIRouter
from services.load_service import *

load_router = APIRouter(prefix="/load", tags=["load"])

#TODO: add optional string input for multiple file names to load into odb_v3 table 
# split by comma and loop through each file name to load into odb_v3 table
@load_router.post("/ODBV3_into_h3_lake")
def load_ODBV3_into_h3_lake():
    # Hardcoded list of ODB_V3 files to bulk load into h3 partitioned parquet data lake
    # Assumes files are inside of map-sandbox/source-data/ODB_v3 folder and are named ODB_v3_{province}.gpkg

    names = ["ON_1", "ON_2", "ON_3"] # ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "ON_1", "ON_2", "ON_3", "PE", "QC_1", "QC_2", "SK", "YT"]
    for name in names:
        file_name = f"ODB_v3_{name}"
        isSuccessful = load_gpkg_to_parquet_lake(file_name)
        if(isSuccessful):
            print(f"{file_name} added to data lake")
        else:
            print(f"{file_name} was not added to data lake")
    return {"success": True }


@load_router.post("/gpkg_into_h3_lake")
def load_gpkg_into_h3_lake(file_name: str):
    # Loads a geopackage file into the h3 partitioned parquet data lake
    # Assumes filepath is inside of map-sandbox/source-data folder and is named {file_name}.gpkg

    res = load_gpkg_to_parquet_lake(file_name)
    return {"success":res }
