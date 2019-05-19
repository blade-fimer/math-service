# coding=utf-8

import os
import sys
import json
import unittest

path = os.path.join(os.path.dirname(__file__), '../')
path = os.path.abspath(path)
if path not in sys.path:
    sys.path.append(path)

from math_service import app


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.uri = 'v1/fibonacci'
        self.client = app.test_client()

    def tearDown(self):
        pass

    def test_positive(self):
        num, res = 5, "[0, 1, 1, 2, 3, 5]"
        result = self.client.get('{}/{}'.format(self.uri, num))
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.get_data().decode()), res)

        num, res = 0, "[0]"
        result = self.client.get('{}/{}'.format(self.uri, num))
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.get_data().decode()), res)

        num, res = 99999999999, "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173, 86267571272]"
        result = self.client.get('{}/{}'.format(self.uri, num))
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.get_data().decode()), res)

    def test_negotive(self):
        num, res = "", ""
        result = self.client.get('{}/{}'.format(self.uri, num))
        self.assertEqual(result.status_code, 404)

        num, res = -1, ""
        result = self.client.get('{}/{}'.format(self.uri, num))
        self.assertEqual(result.status_code, 404)

        num, res = 'abc', ""
        result = self.client.get('{}/{}'.format(self.uri, num))
        self.assertEqual(result.status_code, 404)

if __name__ == '__main__':
    unittest.main()

