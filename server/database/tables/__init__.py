from database.tables.simple_geometry import create_simple_geometry_table 
from database.tables.odb_v3 import create_odb_v3_table

def create_tables(db):
    create_simple_geometry_table(db)
    create_odb_v3_table(db)