import json
import re
from dataclasses import dataclass
from fractions import Fraction
from typing import Optional

COORDINATE_EXPECTED_FORMAT_RE = re.compile(r'^[+-]?\d+\.\d{4,}$')


@dataclass
class GeoCoordinates:
    latitude: Optional[Fraction] = None
    longitude: Optional[Fraction] = None
    
    def __init__(self, latitude: Fraction | str, longitude: Fraction | str):
        """
        :param latitude: latitude
        :param longitude: longitude
        
        If is string, a value should be like "34.9579272"
        """
        if isinstance(latitude, str):
            if COORDINATE_EXPECTED_FORMAT_RE.match(latitude) is None:
                raise ValueError(f"invalid latitude format: {latitude}")
        if isinstance(longitude, str):
            if COORDINATE_EXPECTED_FORMAT_RE.match(longitude) is None:
                raise ValueError(f"invalid longitude format: {longitude}")
        
        self.latitude = Fraction(latitude) if isinstance(latitude, str) else latitude
        self.longitude = Fraction(longitude) if isinstance(longitude, str) else longitude
    
    def __str__(self):
        json_str = json.dumps(self.__dict__)
        return json_str
