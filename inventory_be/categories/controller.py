from flask import request
from inventory_be.helpers import response_helpers as response
from inventory_be.helpers.db_helpers import Psql

def get_all_categories():
    try:
        Psql.reconnect()
        Psql.cur.execute("SELECT * FROM categories")
        result = Psql.cur.fetchall()
        Psql.conn.close()
        print('DATA BEFORE>>>>>>>>>>', result)
        temp = []
        if result:
            for data in result:
                temp.append({
                    'id': data[0],
                    'nama_kategori': data[1]
                })
            return response.ok(temp, 'Berhasil')
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
            Psql.reconnect()
            Psql.cur.execute("SELECT * FROM categories WHERE category_name=%s", (nama_kategori, ))
            result = Psql.cur.fetchone()
            print('DATA BEFORE>>>>>>>>>>', result)
            if result is None:
                Psql.cur.execute("INSERT INTO categories (category_name) VALUES (%s) RETURNING id", (nama_kategori, ))
                Psql.conn.commit()
                result = Psql.cur.fetchone()
                print('DATA>>>>>>>>>>', result)
                Psql.conn.close()
                if result:
                    return response.ok([
                        {
                            'id' : result[0],
                            'nama_kategori': nama_kategori,
                        }
                    ], 'Berhasil')
            return response.bad_request([{
                'message': 'Duplicate data!',
                'code': 38,
                'field': ['nama_kategori']
            }])
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
        Psql.reconnect()
        Psql.cur.execute(f"SELECT * FROM categories WHERE category_name ILIKE '%{keyword}%'")
        result = Psql.cur.fetchall()
        Psql.conn.close()
        print('DATA BEFORE>>>>>>>>>>', result)
        temp = []
        if result:
            for data in result:
                temp.append({
                    'id': data[0],
                    'nama_kategori': data[1]
                })
            return response.ok(temp, 'Berhasil')
    except Exception as e:
        print(e)
        return response.bad_request([{
            'message': 'Unknown Issues!',
            'code': 37,
            'field': []
        }])