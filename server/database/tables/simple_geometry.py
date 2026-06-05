def create_simple_geometry_table(db):
    db.execute("""
        CREATE SEQUENCE simple_geometry_id_sequence START 1;    
        CREATE TABLE IF NOT EXISTS simple_geometry (
               id INTEGER PRIMARY KEY NOT NULL DEFAULT nextval('simple_geometry_id_sequence'),
               geometry GEOMETRY,
               source STRING
               )               
    """)
    # create index if doesnt exist
    try:
        db.execute("""
        CREATE INDEX simple_geometry_r_tree on simple_geometry USING RTREE(geometry)
        """)
    except Exception as e:
        print("Error creating simple_geometry_r_tree index",e)
