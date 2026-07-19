import duckdb
from services.parquet_orchestrator_service import get_h3_indexed_file_paths

def get_tile_data_from_h3_index(z:int, x:int, y:int):
    parquet_file_paths = get_h3_indexed_file_paths(z,x,y)
    return get_vector_layer_from_duckdb(z, x, y, parquet_file_paths)


def get_vector_layer_from_duckdb(z:int, x:int, y:int, parquet_file_paths: list[str]):
    
    # empty paths check
    if not parquet_file_paths:
        return None 
    
    db = duckdb.connect()
    db.execute("""
        INSTALL 'spatial';
        LOAD 'spatial';
    """)
    return db.execute("""
        SELECT ST_AsMVT({
            'geom': ST_AsMVTGeom(
                ST_Transform(
                    ST_GeomFromWKB(geometry), 
                    'EPSG:4326',
                    'EPSG:3857',
                    true),
                ST_Extent(ST_TileEnvelope($1, $2, $3)),
                4096,
                256,
                true
            )
        }, 'odb_v3', 4096, 'geom')
        FROM read_parquet($4)
    """,[z, x, y, parquet_file_paths]).fetchone()


# transform geom from 4326 to 3857