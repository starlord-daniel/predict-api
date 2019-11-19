import os
import json
from pytest import fixture
from endpoints import load_online_model, load_local_model
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
