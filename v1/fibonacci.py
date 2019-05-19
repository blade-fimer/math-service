# coding=utf-8
# Author: Yuan, Hao
# Created on 2019/05/19

import json
from flask_restful import Resource

__all__ = [
    'Fibonacci',
]

def _fib_list():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

class Fibonacci(Resource):
    def get(self, num):
        fib = []
        for item in _fib_list():
            if item > num:
                break
            fib.append(item)
        ret = json.dumps(fib)
        return ret, 200

