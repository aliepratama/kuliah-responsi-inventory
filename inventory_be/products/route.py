from flask import request
from inventory_be.app import app
import inventory_be.helpers.response_helpers as response
from . import controller

@app.route('/products/lists', methods=['POST', 'GET'])
def product_lists():
    if request.method == 'POST':
        return controller.add_product()
    elif request.method == 'GET':
        return controller.get_all_products()
    else:
        return response.bad_request([{
            'message': 'Unknown Issues!',
            'code': 21,
            'field': []
        }])

@app.route('/products/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def product_list(id: int):
    if request.method == 'GET':
        return controller.get_product(id)
    elif request.method == 'PATCH':
        return controller.edit_product(id)
    elif request.method == 'DELETE':
        return controller.delete_product(id)
    else:
        return response.bad_request([{
            'message': 'Unknown Issues!',
            'code': 21,
            'field': []
        }])
