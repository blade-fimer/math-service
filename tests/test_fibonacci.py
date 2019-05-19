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
        self.client = app.test_client()

    def tearDown(self):
        pass

    def test_basic_access(self):
        uri = 'v1/fibonacci'
        num, res = 5, "[0, 1, 1, 2, 3, 5]"
        result = self.client.get('{}/{}'.format(uri, num))
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.get_data().decode()), res)


if __name__ == '__main__':
    unittest.main()

