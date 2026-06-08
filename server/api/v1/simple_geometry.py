from fastapi import APIRouter
from services.geospatial_file_converter_service import *
from services.simple_geometry_service import copy_file_to_table, get_tile_feature_count, get_empty_geom_count_after_clipping, debug_tile

simple_geometry_router = APIRouter(prefix="/simple_geometry", tags=["simple_geometry"])

@simple_geometry_router.post("/geojson")
def convert_geojson(file_name: str):
    # create parquet input file
    res = geojson_to_parquet(file_name)
    # save to duckdb
    copy_file_to_table(file_name)
    return {"success":res }

@simple_geometry_router.get("/check_empty_geom_after_clip/{z}/{x}/{y}")
def check_empty_geom_after_tile_clipping(z:int, x:int, y:int):
    num_records = get_empty_geom_count_after_clipping(z,x,y)
    return ({"get_empty_geom_count_after_clipping": num_records, })

@simple_geometry_router.get("/debug_tile/{z}/{x}/{y}")
def debug(z:int, x:int, y:int):
    res = debug_tile(z,x,y)
    return ({"debug_tile": res, })

@simple_geometry_router.get("/feature_count/{z}/{x}/{y}")
def feature_count(z:int,x:int,y:int):
    feature_count = get_tile_feature_count(z,x,y)
    return {feature_count}