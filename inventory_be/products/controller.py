from flask import request
from inventory_be.helpers import response_helpers as response
from inventory_be.helpers.db_helpers import Psql


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
            Psql.reconnect()
            Psql.cur.execute("INSERT INTO products (product_name, stock, price, category_id, description) VALUES (%s, %s, %s, %s, %s) RETURNING id",
                             (nama_produk, stok, harga, kategori, deskripsi))
            Psql.conn.commit()
            id_new = Psql.cur.fetchone()
            Psql.conn.close()
            print('DATA BEFORE>>>>>>>>>>', id_new)
            if id_new:
                return response.ok([
                    {
                        'id': id_new[0],
                        'nama_produk' : nama_produk,
                        'stok' : stok,
                        'harga' : harga,
                        'deskripsi' : deskripsi,
                        'kategori' : kategori,
                    }
                ], 'Berhasil')
        return response.bad_request([{
            'message': 'Please check your data!',
            'code': 35,
            'field': ['nama_produk', 'stok', 'harga', 'deskripsi', 'kategori']
        }])
    except Exception as e:
        print(e)
        return response.bad_request([{
            'message': 'Please check your data!',
            'code': 36,
            'field': ['nama_produk', 'stok', 'harga', 'deskripsi', 'kategori']
        }])


def get_all_products():
    try:
        Psql.reconnect()
        Psql.cur.execute("SELECT * FROM products")
        result = Psql.cur.fetchall()
        Psql.conn.close()
        print('DATA BEFORE>>>>>>>>>>', result)
        temp = []
        if result:
            for data in result:
                temp.append({
                    'id': data[0],
                    'nama_produk': data[1],
                    'stok': data[2],
                    'harga': data[3],
                    'image_link': data[4],
                    'deskripsi': data[5],
                    'kategori': data[6],
                })
        return response.ok(temp, 'Berhasil')
    except Exception as e:
        print(e)
        return response.bad_request([{
            'message': 'Unknown Issues!',
            'code': 37,
            'field': []
        }])
        
def get_product(id: int):
    try:
        Psql.reconnect()
        Psql.cur.execute("SELECT * FROM products WHERE id=%s", (id, ))
        result = Psql.cur.fetchone()
        Psql.conn.close()
        print('DATA BEFORE>>>>>>>>>>', result)
        if result:
            return response.ok({
                'id': result[0],
                'nama_produk': result[1],
                'stok': result[2],
                'harga': result[3],
                'image_link': result[4],
                'deskripsi': result[5],
                'kategori': result[6],
            }, 'Berhasil')
    except Exception as e:
        print(e)
        return response.bad_request([{
            'message': 'Unknown Issues!',
            'code': 37,
            'field': []
        }])
        
def edit_product(id: int):
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
            Psql.reconnect()
            Psql.cur.execute("UPDATE products SET product_name=%s, stock=%s, price=%s, category_id=%s, description=%s WHERE id=%s",
                             (nama_produk, stok, harga, kategori, deskripsi, id))
            Psql.conn.commit()
            Psql.conn.close()
            print('DATA BEFORE>>>>>>>>>>', id)
            return response.ok([
                {
                    'id': id,
                    'nama_produk' : nama_produk,
                    'stok' : stok,
                    'harga' : harga,
                    'deskripsi' : deskripsi,
                    'kategori' : kategori,
                }
            ], 'Berhasil')
        return response.bad_request([{
            'message': 'Please check your data!',
            'code': 35,
            'field': ['nama_produk', 'stok', 'harga', 'deskripsi', 'kategori']
        }])
    except Exception as e:
        print(e)
        return response.bad_request([{
            'message': 'Please check your data!',
            'code': 36,
            'field': ['nama_produk', 'stok', 'harga', 'deskripsi', 'kategori']
        }])
        
def delete_product(id: int):
    try:
        Psql.reconnect()
        Psql.cur.execute("SELECT * FROM products")
        result = Psql.cur.fetchall()
        if len(result) > 0:
            Psql.cur.execute("DELETE FROM products WHERE id=%s", (id, ))
            Psql.conn.commit()
            Psql.conn.close()
            return response.success('Berhasil menghapus data!')
        else:
            return response.success('Data sudah kosong')
    except Exception as e:
        print(e)
        return response.bad_request([{
            'message': 'Please check your data!',
            'code': 36,
            'field': ['nama_produk', 'stok', 'harga', 'deskripsi', 'kategori']
        }])