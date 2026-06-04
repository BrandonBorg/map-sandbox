import duckdb
from database.tables import create_tables

_db = None

def init_db():
    global _db
    _db = duckdb.connect()
    create_tables(_db)
    
def get_db():
    return _db