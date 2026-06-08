from fastapi import APIRouter
from services.geospatial_file_converter_service import *
from services.simple_geometry_service import copy_file_to_table, get_simple_geometry, get_record_count, get_empty_geom_count_after_clipping, debug_tile

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

@geospatial_file_converter_router.get("/check_empty_geom_after_clip/{z}/{x}/{y}")
def check_empty_geom_after_tile_clipping(z:int, x:int, y:int):
    num_records = get_empty_geom_count_after_clipping(z,x,y)
    return ({"get_empty_geom_count_after_clipping": num_records, })

@geospatial_file_converter_router.get("/debug_tile/{z}/{x}/{y}")
def debug(z:int, x:int, y:int):
    res = debug_tile(z,x,y)
    return ({"debug_tile": res, })