from unittest import TestCase

from .domain import RealEstateListing
from scrape_core.flattener import flatten_dataclass


class TestRealEstateListing(TestCase):
    def test_flatten(self):
        obj = RealEstateListing()
        obj.object_info.domain = 'foo-bar.com'
        obj.features.pool = True
        fl_dict = flatten_dataclass(obj)
        
        assert 'object_info_domain' in fl_dict
        assert fl_dict['object_info_domain'] == 'foo-bar.com'
