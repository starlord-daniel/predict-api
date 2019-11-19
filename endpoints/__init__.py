# api/__init__.py
from flask import Flask
from flask_cors import CORS  # https://flask-cors.readthedocs.io/en/latest/
from .model_helper import predict_from_url, load_online_model, load_local_model
from .routes import simple, pred_route, update_route

api = Flask(__name__)
CORS(api)

# add endpoint paths
api.add_url_rule(
    '/api/predict',
    view_func=pred_route,
    methods=['POST']
)

api.add_url_rule(
    '/api/update',
    view_func=update_route,
    methods=['POST']
)

# register your blueprints here
api.register_blueprint(simple)
