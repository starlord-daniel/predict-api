from flask import Blueprint, make_response, request, jsonify
from flask.views import MethodView
import json

from endpoints import api
from ..model_helper import predict_from_url, load_online_model

simple = Blueprint('simple', __name__)

# load config
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# load model
model = load_online_model(config['model_url'], config['filepath'])


class PredictionRoute(MethodView):
    def post(self):
        if request.json is None:
            return make_response('Please set the Content-Type to \
                application/json', 406)
        try:
            input_params = request.json

            # load image from url
            url = input_params['url']
            prediction = predict_from_url(url, model)

            response = make_response(json.dumps(prediction, indent=4), 200)
            response.headers['Content-Type'] = 'application/json'

            return response
        except Exception as e:
            return make_response(f'An error did occur: {str(e)}'.format, 500)


pred_route = PredictionRoute.as_view('pred_route')
api.add_url_rule(
    '/api/predict',
    view_func=pred_route,
    methods=['POST']
)


class UpdateRoute(MethodView):
    def post(self):
        global model
        if request.json is None:
            return make_response(
                'Please set the Content-Type to application/json', 406)
        try:
            input_params = request.json

            if(config['update_key'] == input_params['key']):
                model = load_online_model(
                    config['model_url'],
                    config['filepath'])
                output = {"message": "Model update successful :-)"}
            else:
                output = {"message": "Model update un-successful :-("}

            response = make_response(json.dumps(output, indent=4), 200)
            response.headers['Content-Type'] = 'application/json'

            return response
        except Exception as e:
            return make_response(f'An error did occur: {str(e)}', 500)


update_route = UpdateRoute.as_view('update_route')
api.add_url_rule(
    '/api/update',
    view_func=update_route,
    methods=['POST']
)
