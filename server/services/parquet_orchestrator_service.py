import mercantile
import h3
from constants.tiles_constants import H3_LAKE_FOLDER, H3_PARTITION_RES

def get_h3_indexed_file_paths(z:int, x:int, y:int):
    '''
    uzing tile z x y
    
    RETURNS
    -------
    parquet_file_paths:
        array of strings containing parquet file paths for the given h3 index
    '''
    h3_index_arry = get_h3_indexes_for_tile(z,x,y)
    return get_parquet_file_paths_from_h3_index_array(h3_index_arry)

def get_h3_indexes_for_tile(z:int, x:int, y:int, h3_res = H3_PARTITION_RES):
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


    return h3.h3shape_to_cells_experimental(boundary_polygon, h3_res, "overlap")

def get_parquet_file_paths_from_h3_index_array(h3_index_array: list[str], h3_lake_folder = H3_LAKE_FOLDER):
    ''' 
    Returns
    -------
    parquet_file_paths:
        array of strings containing parquet file paths for the given h3 index
    '''

    return [h3_lake_folder + h3_index + "/*.parquet" for h3_index in h3_index_array ]

