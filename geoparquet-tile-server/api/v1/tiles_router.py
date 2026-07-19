# import gzip
from fastapi import APIRouter

from services.tile_service import get_tile_data_from_h3_index
from fastapi.responses import Response

tiles_router = APIRouter(prefix="/tiles", tags=["tiles"])


#https://gist.github.com/Maxxen/37e4a9f8595ea5e6a20c0c8fbbefe955
@tiles_router.get("/{z}/{x}/{y}")
def get_tiles(z:int,x:int,y:int):

    row = get_tile_data_from_h3_index(z,x,y)

    # send tile data as response
    if row is None:
        return Response(
            content=b"",
            media_type= "application/vnd.mapbox-vector-tile"
        )
          
    tile = row[0]

    # option for zipping response 
    # tile = gzip.compress(row[0])

    return Response(
        content=tile,
        media_type="application/vnd.mapbox-vector-tile",
        #  headers={"Content-Encoding": "gzip"}
    )
