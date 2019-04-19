
from flask import jsonify


def success(data=None):
    r = {'code': 200, 'data': data if (data != None) else 'Success'}
    return jsonify(r)