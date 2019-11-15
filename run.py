# server is used for development purposes and should only be used there
# for production environments:
# https://flask.palletsprojects.com/en/master/tutorial/deploy/

from flask import Flask, jsonify, abort, request, make_response, url_for
from endpoints import api

wsgi_app = api.wsgi_app

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '8000'))
    except ValueError:
        PORT = 5555
    # to run on https: api.run(HOST, PORT, ssl_context='adhoc')
    api.run(HOST, PORT)
