from flask import request
from inventory_be.app import app
from . import controller

@app.route('/categories/lists', methods=['GET', 'POST'])
def lists():
    if request.method == 'GET':
        return controller.get_all_categories()
    elif request.method == 'POST':
        return controller.add_category()
    else:
        return 'gagal'

@app.route('categories/<str:keyword>', methods=['POST'])
def search(keyword: str):
    if request.method == 'POST':
        return controller.search_category(keyword)
    return 'gagal'
