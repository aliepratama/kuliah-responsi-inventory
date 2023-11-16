from psycopg2 import connect

class PsqlApp:
    def __init__(self):
        self.conn = connect(
            database='inventory',
            host='localhost',
            port='5432',
            user='aliepratama',
            password='password',
        )

        self.cur = self.conn.cursor()
    
    def reconnect(self):
        self.conn = connect(
            database='inventory',
            host='localhost',
            port='5432',
            user='aliepratama',
            password='password',
        )
        self.cur = self.conn.cursor()

Psql = PsqlApp()
