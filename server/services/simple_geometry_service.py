from database.connection import get_db

def copy_file_to_table(file_name):
    db = get_db()
    file_path = f"files/output/{file_name}.parquet"
    return db.execute(f"""
        INSERT INTO simple_geometry (
                        geometry,
                        source,
                        geometry_3857
                      )
        SELECT geometry, source, ST_Simplify(ST_Transform(geometry,'EPSG:4326','EPSG:3857',true),10) AS geometry_3857
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
            ST_AsText(geometry_3857) AS geometry_3857,
            source
        FROM simple_geometry
        LIMIT 100                  
    """).fetchall()

# need to re work from here https://duckdb.org/docs/current/core_extensions/spatial/functions#st_asmvt
def get_tile_data(z:int, x:int, y:int):
    db = get_db()
    return db.execute("""
    WITH tile_Data AS (
        SELECT {
            'geometry': ST_AsMVTGeom
                    (
                        geometry_3857,
                        ST_Extent(ST_TileEnvelope($1, $2, $3)),
                            4096,
                            64,
                            true
                    ),
                'source': TRY_CAST("source" AS VARCHAR),
        } AS feature
        FROM simple_geometry
        WHERE ST_Intersects(
        geometry_3857,
        ST_TileEnvelope($1, $2, $3)
        )
    )
    
    SELECT ST_AsMVT(
        feature,
        'simple_geometry', -- layer name
         4096,
        'geometry'
    ) AS mvt
    FROM tile_data;
   
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