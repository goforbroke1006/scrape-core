import json
from unittest import TestCase
from dataclasses import asdict

from scrape_core.common import scrape_result_serializer
from .domain import RealEstateListing
from scrape_core.flattener import flatten_dataclass


class TestRealEstateListing(TestCase):
    def test_flatten(self):
        obj = RealEstateListing()
        obj.provider = 'foo-bar.com'
        obj.property_features.pool = True
        fl_dict = flatten_dataclass(obj)
        
        assert 'object_info_domain' in fl_dict
        assert fl_dict['provider'] == 'foo-bar.com'
        assert fl_dict['property_features_pool'] == 'foo-bar.com'
        
    def test_json_serialize_and_deserialize(self):
        obj = RealEstateListing()
        obj.provider = 'foo-bar.com'
        obj.property_features.pool = True
        
        json_dict = json.loads(json.dumps(obj, default=scrape_result_serializer))
        
        assert 'provider' in json_dict
        assert json_dict['provider'] == 'foo-bar.com'
        assert json_dict['property_features']['pool'] == True
