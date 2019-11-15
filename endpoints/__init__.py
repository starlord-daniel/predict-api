# api/__init__.py
from flask import Flask
from flask_cors import CORS  # https://flask-cors.readthedocs.io/en/latest/
from .model_helper import predict_from_url
from .routes.main import api, simple

api = Flask(__name__)
CORS(api)

# register your blueprints here
api.register_blueprint(simple)
