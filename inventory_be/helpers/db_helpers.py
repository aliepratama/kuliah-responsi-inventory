from psycopg2 import connect

conn = connect(
    database='inventory',
    host='localhost',
    port='5432',
    user='aliepratama',
    password='Aw!kw0k000',
)

cur = conn.cursor() 