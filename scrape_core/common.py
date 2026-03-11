from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List

from scrape_core.contract.prime.country_code.country_code import CountryAlpha2Code
from scrape_core.contract.prime.price.price_info import PriceInfo


@dataclass
class MediaInfo:
    photos: List[str] = field(default_factory=list)
    videos: List[str] = field(default_factory=list)


from dataclasses import dataclass
from typing import get_type_hints, Union, get_origin, get_args


class StrictTypes:
    def __setattr__(self, key, value):
        hints = get_type_hints(self.__class__)
        
        if key in hints and value is not None:
            expected = hints[key]
            
            if not _check_type(value, expected):
                raise TypeError(
                    f"{key} must be {expected}, got {type(value)}"
                )
        
        super().__setattr__(key, value)


def _check_type(value, expected):
    origin = get_origin(expected)
    
    if origin is Union:
        return any(_check_type(value, t) for t in get_args(expected))
    
    if isinstance(expected, type):
        return isinstance(value, expected)
    
    return True


@dataclass
class ScrapeResult(StrictTypes):
    provider: Optional[str] = None
    details_url: Optional[str] = None
    
    categories: Optional[List[str]] = None
    
    country: Optional[CountryAlpha2Code] = None
    
    title: Optional[str] = None
    description_text: Optional[str] = None
    
    price_primary: PriceInfo = field(default_factory=PriceInfo)
    price_secondary: PriceInfo = field(default_factory=PriceInfo)
    
    scraped_at: Optional[datetime] = None
    
    media: MediaInfo = field(default_factory=MediaInfo)
    
    robots_txt_allows: bool = False
