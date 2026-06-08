def create_odb_v3_table(db):
    db.execute("""
        CREATE TABLE IF NOT EXISTS odb_v3 (
                id VARCHAR,
                source_id VARCHAR,
                source VARCHAR,
                dataset VARCHAR,
                csduid VARCHAR,
                csdname VARCHAR,
                prov_terr VARCHAR,
                name VARCHAR,
                type VARCHAR,
                address VARCHAR,
                year_built INTEGER,
                units INTEGER,
                floors INTEGER,
                sq_ft DOUBLE,
                height DOUBLE,
                geometry GEOMETRY, --- EPSG:3347
                geometry_3857 GEOMETRY
        )               
    """)
    # create index if doesnt exist
    try:
        db.execute("""
        CREATE INDEX IF NOT EXISTS odb_v3_r_tree on odb_v3 USING RTREE(geometry_3857)
        """)
    except Exception as e:
        print("Error creating odb_v3_r_tree index",e)
