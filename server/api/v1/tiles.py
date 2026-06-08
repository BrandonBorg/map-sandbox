import gzip
import time
from fastapi import APIRouter
from services.simple_geometry_service import get_tile_data
from services.odb_v3_service import get_odb_v3_tile_data
from fastapi.responses import Response

tiles_router = APIRouter(prefix="/tiles", tags=["tiles"])



#https://gist.github.com/Maxxen/37e4a9f8595ea5e6a20c0c8fbbefe955
@tiles_router.get("/simple_geometry/{z}/{x}/{y}")
def get_tiles(z:int,x:int,y:int):

    start = time.time()
    row = get_tile_data(z,x,y)

    # send tile data as response
    if row is None:
        print(f"{z}/{x}/{y} size 0 took {time.time()-start:.2f}s")
        return Response(
            content=b"",
            media_type= "application/vnd.mapbox-vector-tile"
        )
          
    tile = gzip.compress(row[0])
    print(
        f"{z}/{x}/{y} raw={len(row[0])} "
        f"gzipped={len(tile)}"
        f"took {time.time()-start:.2f}s"
    )

    return Response(
        content=tile,
        media_type="application/vnd.mapbox-vector-tile",
        headers={"Content-Encoding": "gzip"}
    )

@tiles_router.get("/odb_v3/{z}/{x}/{y}")
def get_tiles(z:int,x:int,y:int):

    start = time.time()
    row = get_odb_v3_tile_data(z,x,y)

    # send tile data as response
    if row is None:
        print(f"{z}/{x}/{y} size 0 took {time.time()-start:.2f}s")
        return Response(
            content=b"",
            media_type= "application/vnd.mapbox-vector-tile"
        )
          
    tile = gzip.compress(row[0])
    print(
        f"{z}/{x}/{y} raw={len(row[0])} "
        f"gzipped={len(tile)}"
        f"took {time.time()-start:.2f}s"
    )

    return Response(
        content=tile,
        media_type="application/vnd.mapbox-vector-tile",
        headers={"Content-Encoding": "gzip"}
    )
