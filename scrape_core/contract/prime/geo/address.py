from dataclasses import dataclass
from typing import Optional

from prime.geo.obj_value import CountryAlpha2Code


@dataclass
class AddressInfoDTO:
    text: Optional[str] = None
    
    country: Optional[CountryAlpha2Code] = None
    state: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    neighborhood: Optional[str] = None
    
    