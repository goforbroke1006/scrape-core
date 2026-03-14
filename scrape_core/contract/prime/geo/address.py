from dataclasses import dataclass
from typing import Optional

from ..country_code.country_code import CountryAlpha2Code


@dataclass
class AddressInfo:
    text: Optional[str] = None
    
    country: Optional[CountryAlpha2Code] = None
    state: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    neighborhood: Optional[str] = None
    zip_code: Optional[str] = None
    
    island_name: Optional[str] = None
