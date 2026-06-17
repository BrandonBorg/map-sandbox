import mercantile
import h3
from constants.tiles_constants import H3_LAKE_FOLDER, H3_PARTITION_RES


def create_duck_db_connection(z:int, x:int, y:int):
    '''    TODO

    '''
    return

def get_h3_indexs_for_tile(z:int, x:int, y:int):
    '''
    Note
    ----
    With current h3 res = 6 at time of writting, zoom level can be to high such that tile range is smaller than an h3 hex of res 6
    this will return empty cells array.
        Because of this, I have decided to use experimental for now to set containment to overlap.

        This will ofcourse result in more cells at lower zoom levels but each cell has very limited data for now 
        so I suspect  we will be fine...

    Returns
    -------
    h3_index_arry:
        array of res 6 h3 index that are within the tile 
    '''
    # get bounds from tile location using mercantile
    bounds = mercantile.bounds(x, y, z)

    boundary_polygon = h3.LatLngPoly(
    [(bounds.south, bounds.west),
    (bounds.south, bounds.east),
    (bounds.north, bounds.east),
    (bounds.north, bounds.west)],
    )


    return h3.h3shape_to_cells_experimental(boundary_polygon, H3_PARTITION_RES, "overlap")



def get_parquet_file_paths_from_h3_index_array(h3_index_array: list[str]):
    '''    TODO

    '''
    return

def init_duckdb_with_parquet_file_paths(parquet_file_paths: list[str]):
    '''    TODO
    '''
    return