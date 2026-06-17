import duckdb
from database.tables import create_tables

db_path = "database/database.duckdb"
_db = None

# initializes db instance
def init_db():
    global _db
    _db = duckdb.connect(db_path)
    init_extensions(_db)
    create_tables(_db)

# installs and loads all needed extensions
def init_extensions(db):
    db.execute("""
        INSTALL 'spatial';
        LOAD 'spatial';
    """)

# gets db instance
def get_db(db_path):
    db = duckdb.connect(db_path)
    init_extensions(db)
    return db
