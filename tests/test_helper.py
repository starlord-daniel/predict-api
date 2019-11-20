import os
import json
import requests
from pytest import fixture
from endpoints import load_online_model, load_local_model, predict_from_url
from endpoints.models.net import Net


class TestHelper(object):
    '''
    Test methods from model_helper file.
    '''
    config = {}

    @fixture(scope="function", autouse=True)
    def load_test_config(self):
        with open("tests/config-testing.json", "r") as config_file:
            self.config = json.load(config_file)

    def test_load_local_model(self):
        model_path = self.config['model_path']
        test_model = load_local_model(model_path)
        assert(type(test_model) == Net)
        assert isinstance(test_model, Net)

    def test_load_online_image(self):
        test_image_url = self.config['test_image_url']
        url_response = requests.get(test_image_url)
        assert(url_response.status_code == 200)

    def test_model_outcome(self):
        model_path = self.config['model_path']
        test_image_url = self.config['test_image_url']
        test_model = load_local_model(model_path)
        predictions = predict_from_url(test_image_url, test_model)
        assert(len(predictions.keys()) == 10)
        assert(predictions['dog'] == 0)
        assert(predictions['truck'] == 1)
