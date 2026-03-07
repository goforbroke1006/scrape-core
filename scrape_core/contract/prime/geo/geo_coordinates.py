import json
import re
from fractions import Fraction

COORDINATE_EXPECTED_FORMAT_RE = re.compile(r'^[+-]?\d+\.\d{6,}$')


class GeoCoordinates:
    def __init__(self, latitude: Fraction | str, longitude: Fraction | str):
        """
        :param latitude: latitude
        :param longitude: longitude
        
        If is string, a value should be like "34.9579272"
        """
        if isinstance(latitude, str):
            if COORDINATE_EXPECTED_FORMAT_RE.match(latitude) is None:
                raise ValueError("Invalid latitude format")
        if isinstance(longitude, str):
            if COORDINATE_EXPECTED_FORMAT_RE.match(longitude) is None:
                raise ValueError("Invalid longitude format")
        
        self.latitude = latitude
        self.longitude = longitude
    
    def __str__(self):
        json_str = json.dumps(self.__dict__)
        return json_str
