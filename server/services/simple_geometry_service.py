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

