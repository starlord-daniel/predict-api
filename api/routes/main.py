from flask import Blueprint, make_response, request, jsonify
from flask.views import MethodView

from api import api
from api.model_helper import load_model, predict_from_url

import json

simple = Blueprint('simple', __name__)

# load model
model = load_model('api/data/simple_cnn.pth')

class PredictionRoute(MethodView):
    def post(self):
        if request.json == None:
            return make_response('Please set the Content-Type to application/json', 406)
        try:
            input_params = request.json

            # load image from url
            url = input_params['url']
            prediction = predict_from_url(url, model)
            
            response = make_response(json.dumps(prediction, indent=4), 200)
            response.headers['Content-Type'] = 'application/json'

            return response
        except Exception as e:
            return make_response('An error did occur: {m}'.format(m = str(e)), 500)

pred_route =  PredictionRoute.as_view('pred_route')
api.add_url_rule(
    '/api/predict', view_func=pred_route, methods=['POST']
)

class UpdateRoute(MethodView):
    def post(self):
        if request.json == None:
            return make_response('Please set the Content-Type to application/json', 406)
        try:
            input_params = request.json
            
            # create empty output
            output = {}

            # download the model and save
            filepath = input_params['model_url']
            # TODO: SAVE MODEL

            # load the new model
            model = load_model(filepath)

            # verify the new model

            # if verification ok:
            if (True):
                # replace the new model
                
                # Return success message
                output = { "message": "Model update successful :-)"}
            else:
                # return error message
                output = { "message": "Model update failed :-("}
                
            
            response = make_response(json.dumps(output, indent=4), 200)
            response.headers['Content-Type'] = 'application/json'
            
            return response
        except Exception as e:
            return make_response('An error did occur: {m}'.format(m = str(e)), 500)



update_route =  UpdateRoute.as_view('update_route')
api.add_url_rule(
    '/api/update', view_func=update_route, methods=['POST']
)