from flask import request
from inventory_be.helpers import response_helpers as response


def add_product():
    try:
        try:
            nama_produk = request.form['nama_produk']
            stok = request.form['stok']
            harga = request.form['harga']
            deskripsi = request.form['deskripsi']
            kategori = request.form['kategori']
        except Exception as e:
            print(e)
            return response.bad_request([{
                'message': 'Please check your data!',
                'code': 35,
                'field': ['nama_produk', 'stok', 'harga', 'deskripsi', 'kategori']
            }])
        if all((nama_produk, stok, harga, kategori)):
            return response.ok([
                {
                    'nama_produk' : nama_produk,
                    'stok' : stok,
                    'harga' : harga,
                    'deskripsi' : deskripsi,
                    'kategori' : kategori,
                }
            ], 'Berhasil')
    except Exception as e:
        print(e)
        return response.bad_request([{
            'message': 'Please check your data!',
            'code': 36,
            'field': ['nama_produk', 'stok', 'harga', 'deskripsi', 'kategori']
        }])


def get_all_products():
    try:
        return response.ok([], 'Berhasil')
    except Exception as e:
        print(e)
        return response.bad_request([{
            'message': 'Unknown Issues!',
            'code': 37,
            'field': []
        }])
        
def get_product(id: int):
    pass
        
def edit_product(id: int):
    pass
        
def delete_product(id: int):
    pass