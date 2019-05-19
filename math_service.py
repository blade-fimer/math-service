#!/usr/bin/python
# coding=utf-8

import argparse

from flask import Flask
from flask_restful import Api

# API list
from v1.fibonacci import Fibonacci


app = Flask(__name__)
api = Api(app)

api.add_resource(Fibonacci, '/v1/fibonacci/<int:num>')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Providing math related RESTful API service.')
    parser.add_argument('--debug', '-d', help='debug version', action='store_true')
    parser.add_argument('--conf', '-c', help='configuration file path')
    args = parser.parse_args()

    os.chdir(os.path.dirname(__file__))
#    app.logger.info('Running...')
    if args.conf:
        # TODO: read server configuration
        pass
    app.run(host='0.0.0.0', port=8080, debug = True if args.debug else False)
