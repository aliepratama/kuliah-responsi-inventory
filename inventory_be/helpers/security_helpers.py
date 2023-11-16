from flask_cors import CORS
from inventory_be.app import app

cors = CORS(app, resources={r"/products/*": {"origins": "*"}})
cors = CORS(app, resources={r"/categories/*": {"origins": "*"}})
