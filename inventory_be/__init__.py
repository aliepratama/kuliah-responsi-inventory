from inventory_be.helpers.db_helpers import conn, cur
from inventory_be.app import app
print('ROOT>>>>>>>>>>>', __name__)
import inventory_be.products

if __name__ == '__main__':
    cur.execute('SELECT * FROM products')
    print(cur.fetchall())
    app.run(debug=True)