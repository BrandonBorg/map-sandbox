import mercantile
import h3
from constants.tiles_constants import H3_LAKE_FOLDER, H3_PARTITION_RES

def create_duck_db_connection(z:int, x:int, y:int):
    '''    TODO

    '''
    return

def get_h3_indexs_for_tile(z:int, x:int, y:int):
    '''
    Returns
    -------
    h3_index_arry:
        array of res 6 h3 index that are within the tile 
    '''
    # get bounds from tile location using mercantile
    bounds = mercantile.bounds(x, y, z)

    boundary_polygon = h3.LatLngPoly([
        (bounds.north, bounds.west),
        (bounds.north, bounds.east),
        (bounds.south, bounds.east),
        (bounds.south, bounds.west),
    ])

    return h3.polygon_to_cells(boundary_polygon, H3_PARTITION_RES)



def get_parquet_file_paths_from_h3_index_array(h3_index_array: list[str]):
    '''    TODO

    '''
    return

def init_duckdb_with_parquet_file_paths(parquet_file_paths: list[str]):
    '''    TODO
    '''
    return