from flask import jsonify, make_response
print('REF>>>>>>>>>>>', __name__)


def ok(data: any, message: str) -> any:
    res = {
        'message': message,
        'data': data,
    }
    return make_response(jsonify(res), 200)


def success(message: str) -> any:
    res = {
        'message': message
    }
    return make_response(jsonify(res), 201)


def bad_request(values: any) -> any:
    res = {
        'message': 'Validation errors in your request',
        'errors': values,
    }
    return make_response(jsonify(res), 400)
