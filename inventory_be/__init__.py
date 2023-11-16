from inventory_be.app import app
from inventory_be.helpers.security_helpers import cors
import inventory_be.products
import inventory_be.categories

if __name__ == '__main__':
    app.run(debug=True)