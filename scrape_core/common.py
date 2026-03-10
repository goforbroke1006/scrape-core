from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List

from scrape_core.contract.prime.price.price_info import PriceInfo


@dataclass
class MediaInfo:
    photos: List[str] = field(default_factory=list)
    videos: List[str] = field(default_factory=list)


@dataclass
class ScrapeResult:
    provider: Optional[str] = None
    details_url: Optional[str] = None
    
    categories: Optional[List[str]] = None
    
    title: Optional[str] = None
    description_text: Optional[str] = None
    
    price_primary: PriceInfo = field(default_factory=PriceInfo)
    price_secondary: PriceInfo = field(default_factory=PriceInfo)
    
    scraped_at: Optional[datetime] = None
    
    media: MediaInfo = field(default_factory=MediaInfo)
    
    robots_txt_allows: bool = False
