import gzip
from fastapi import APIRouter
from services.simple_geometry_service import get_tile_data, get_tile_feature_count
from fastapi.responses import Response
import gzip
import time
tiles_router = APIRouter(prefix="/tiles", tags=["tiles"])



#https://gist.github.com/Maxxen/37e4a9f8595ea5e6a20c0c8fbbefe955
@tiles_router.get("/simple_geometry/{z}/{x}/{y}")
def get_tiles(z:int,x:int,y:int):

    
    start = time.time()
    row = get_tile_data(z,x,y)
    
    # send tile data as response
    if row is None is None:
        print(f"{z}/{x}/{y} size 0 took {time.time()-start:.2f}s")
        return Response(
            content=b"",
            media_type= "application/vnd.mapbox-vector-tile"
        )
          
    print(f"{z}/{x}/{y} size {len(row[0])} took {time.time()-start:.2f}s")


    return Response(
        content=gzip.compress(row),
        media_type="application/vnd.mapbox-vector-tile",
        headers={"Content-Encoding": "gzip"}
    )

@tiles_router.get("/feature_count/{z}/{x}/{y}")
def get_tiles(z:int,x:int,y:int):
    feature_count = get_tile_feature_count(z,x,y)
    return {feature_count}
