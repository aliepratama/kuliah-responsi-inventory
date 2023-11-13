from flask import request
from inventory_be.helpers import response_helpers as response

def get_all_categories():
    try:
        return response.ok([], 'Berhasil')
    except Exception as e:
        print(e)
        return response.bad_request([{
            'message': 'Unknown Issues!',
            'code': 37,
            'field': []
        }])

def add_category():
    try:
        try:
            nama_kategori = request.form['nama_kategori']
        except Exception as e:
            print(e)
            return response.bad_request([{
                'message': 'Please check your data!',
                'code': 35,
                'field': ['nama_kategori']
            }])
        if nama_kategori:
            return response.ok([
                {
                    'id' : '',
                    'nama_kategori': nama_kategori,
                }
            ], 'Berhasil')
        return response.bad_request([{
            'message': 'Please check your data!',
            'code': 35,
            'field': ['nama_kategori']
        }])
    except Exception as e:
        print(e)
        return response.bad_request([{
            'message': 'Please check your data!',
            'code': 36,
            'field': ['nama_kategori']
        }])

def search_category(keyword: str):
    try:
        return response.ok([], 'Berhasil')
    except Exception as e:
        print(e)
        return response.bad_request([{
            'message': 'Unknown Issues!',
            'code': 37,
            'field': []
        }])