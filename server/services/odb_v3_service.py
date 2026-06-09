
from database.connection import get_db


def get():
    db = get_db()
    return db.execute("""
        SELECT ST_AsText(geometry_3857) as geometry_3857, ST_AsText(geometry) as geometry
        FROM odb_v3
        LIMIT 100               
    """).fetchall()

def clear_table():
    db = get_db()
    return db.execute("""
        DELETE FROM odb_v3            
    """)
    

def get_record_count():
    db = get_db()
    return db.execute("""
        SELECT COUNT() as total_records
        FROM odb_v3;                  
    """).fetchone()



def copy_file_to_odb_v3(file_name, db):
    file_path = f"files/output/{file_name}.parquet"
    return db.execute(f"""
        INSERT INTO odb_v3 
        SELECT t.*, ST_Transform(geometry,'EPSG:3347','EPSG:3857',true) AS geometry_3857
        FROM read_parquet('{file_path}') t           
    """)



def get_odb_v3_tile_data(z:int, x:int, y:int):
    db = get_db()
    return db.execute("""
        SELECT ST_AsMVT({
            'geom': ST_AsMVTGeom(
                geometry_3857,
                ST_Extent(ST_TileEnvelope($1, $2, $3)),
                4096,
                256,
                true
            )
        }, 'odb_v3', 4096, 'geom' )
        FROM odb_v3 WHERE ST_Intersects(geometry_3857, ST_TileEnvelope($1, $2, $3))
    """,[z, x, y]).fetchone()
