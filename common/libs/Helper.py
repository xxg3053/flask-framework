
from flask import jsonify


def success(data=None):
    return jsonify({'code': 200, 'data': data if (data is not None) else 'Success'})

def fail(code=400, message='Fail'):
    return jsonify({'code': code, 'data': message})