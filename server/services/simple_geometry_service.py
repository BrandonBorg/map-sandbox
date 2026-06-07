from database.connection import get_db

def copy_file_to_table(file_name):
    db = get_db()
    file_path = f"files/output/{file_name}.parquet"
    return db.execute(f"""
        INSERT INTO simple_geometry (geometry, source)
        SELECT *
        FROM read_parquet('{file_path}')           
    """)

def get_record_count():
    db = get_db()
    return db.execute("""
        SELECT COUNT() as total_records
        FROM simple_geometry;                  
    """).fetchone()

def get_simple_geometry():
    db = get_db()
    return db.execute("""
        SELECT 
            id,
            ST_AsText(geometry) AS geometry,
            source
        FROM simple_geometry
        LIMIT 100                  
    """).fetchall()

# todo redo this entire function
def get_tile_data(z:int, x:int, y:int):
    db = get_db()
    return db.execute("""
    WITH tile_Data AS (
        SELECT {
            'geometry': ST_AsMVTGeom
                    (
                        ST_Transform(geometry,'EPSG:4326', 'EPSG:3857', true),
                        ST_Extent(ST_TileEnvelope($1, $2, $3))
                    ),
                'source': TRY_CAST("source" AS VARCHAR),
            } AS feature
        FROM simple_geometry
        WHERE geometry IS NOT NULL
        AND ST_Intersects(
            ST_Transform(geometry, 'EPSG:4326', 'EPSG:3857', true),
            ST_TileEnvelope($1, $2, $3)
        )
    )
    
    SELECT ST_AsMVT(
        feature,
        'simple_geometry', -- layer name
        4096,
        'geometry'
    ) AS mvt
    FROM tile_data
    WHERE feature.geometry IS NOT NULL AND NOT ST_IsEmpty(feature.geometry);
    """,[z, x, y]).fetchone()



def get_tile_feature_count(z:int, x:int, y:int):
    db = get_db()
    return db.execute("""
       SELECT COUNT() as total_records
            FROM simple_geometry 
            WHERE ST_Intersects(
                    ST_Transform(geometry, 'EPSG:4326', 'EPSG:3857', true),
                    ST_TileEnvelope($1, $2, $3))
    """,[z, x, y]).fetchone()


#"
#   SELECT * 
#       FROM simple_geometry
#       WHERE ST_Intersects(geometry, ST_TileEnvelope({z}, {x}, {y}))
# "