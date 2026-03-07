from unittest import TestCase

from complex.real_estate.domain import RealEstateListingDTO
from flattener import flatten_dataclass


class TestRealEstateListingDTO(TestCase):
    def test_flatten(self):
        obj = RealEstateListingDTO()
        obj.object_info.domain = 'foo-bar.com'
        obj.features.pool = True
        fl_dict = flatten_dataclass(obj)
        
        assert 'object_info_domain' in fl_dict
        assert fl_dict['object_info_domain'] == 'foo-bar.com'
