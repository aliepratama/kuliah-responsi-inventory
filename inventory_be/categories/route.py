from flask import request
from inventory_be.app import app
import inventory_be.helpers.response_helpers as response
from . import controller

@app.route('/categories/lists', methods=['GET', 'POST'])
def categories_lists():
    if request.method == 'GET':
        return controller.get_all_categories()
    elif request.method == 'POST':
        return controller.add_category()
    else:
        return response.bad_request([{
            'message': 'Unknown Issues!',
            'code': 21,
            'field': []
        }])

@app.route('/categories/search/<keyword>', methods=['GET'])
def categories_search(keyword: str):
    if request.method == 'GET':
        return controller.search_category(keyword)
    return response.bad_request([{
            'message': 'Unknown Issues!',
            'code': 21,
            'field': []
        }])
