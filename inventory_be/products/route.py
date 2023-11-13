from flask import request
from inventory_be.app import app
from . import controller

@app.route('/products/lists', methods=['POST', 'GET'])
def lists():
    if request.method == 'POST':
        return controller.add_product()
    elif request.method == 'GET':
        return controller.get_all_products()
    else:
        return 'gagal'

@app.route('/products/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def list(id: int):
    if request.method == 'GET':
        return controller.get_product(id)
    elif request.method == 'PATCH':
        return controller.edit_product(id)
    elif request.method == 'DELETE':
        return controller.delete_product(id)
    else:
        return 'gagal'
