from database.tables.test import create_test_table
from database.tables.simple_geometry import create_simple_geometry_table

def create_tables(db):
    create_test_table(db)
    create_simple_geometry_table(db)