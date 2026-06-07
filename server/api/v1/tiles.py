import gzip
from fastapi import APIRouter
from services.simple_geometry_service import get_tile_data, get_tile_feature_count
from fastapi.responses import Response

tiles_router = APIRouter(prefix="/tiles", tags=["tiles"])

#https://gist.github.com/Maxxen/37e4a9f8595ea5e6a20c0c8fbbefe955
@tiles_router.get("/simple_geometry/{z}/{x}/{y}.pbf")
def get_tiles(z:int,x:int,y:int):
    row = get_tile_data(z,x,y)
    
    # send tile data as response
    if row is None or row[0] is None:
        return Response(
            content=b"",
            media_type="application/x-protobuf"
        )

    return Response(
        content=row[0],
        media_type="application/x-protobuf"
    )

@tiles_router.get("/feature_count/{z}/{x}/{y}")
def get_tiles(z:int,x:int,y:int):
    feature_count = get_tile_feature_count(z,x,y)
    return {feature_count}
