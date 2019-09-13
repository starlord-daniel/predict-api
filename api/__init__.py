# api/__init__.py
from flask import Flask
from flask_cors import CORS # https://flask-cors.readthedocs.io/en/latest/

api = Flask(__name__)
CORS(api)

# register your blueprints here
from api.routes.main import *
api.register_blueprint(simple)