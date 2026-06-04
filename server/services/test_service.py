from database.connection import get_db

def insert_user(user: str):
    db = get_db()
    return  db.execute(
        "INSERT INTO test (name) VALUES (?)",
        [user]
    )

def fetch_user(user:str):
    db = get_db()
    return db.execute(
        "SELECT * FROM test WHERE name = ?",
        [user]
    ).fetchone()

def fetch_all_users():
    db = get_db()
    return db.execute(
         "SELECT * FROM test"
    ).fetchall()