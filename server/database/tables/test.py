# creates test table containing id and name
def create_test_table(db):
    db.execute("""
        CREATE SEQUENCE IF NOT EXISTS id_sequence START 1;    
        CREATE TABLE IF NOT EXISTS test (
               id INTEGER PRIMARY KEY NOT NULL DEFAULT nextval('id_sequence'),
               name STRING
               )               
    """)
