import duckdb

class Database:
    def __init__(self):
        self.con = duckdb.connect()
        self.init()
    
    def init(self):
        self.con.execute("INSTALL spatial;") 
        self.con.execute("LOAD spatial;")