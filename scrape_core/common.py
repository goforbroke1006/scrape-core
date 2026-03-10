from dataclasses import dataclass, field
from datetime import datetime
from fractions import Fraction
from typing import Dict, Tuple, Any, Optional, List


@dataclass
class ScrapeResult:
    """Information about the website where the listing was found"""
    provider: Optional[str] = None
    details_url: Optional[str] = None
    
    categories: Optional[List[str]] = None
    
    scraped_at: Optional[datetime] = None


# @dataclass
# class ScrapeObjectInfoDTO:
#     """Information about the website where the listing was found"""
#     domain: Optional[str] = None
#     details_url: Optional[str] = None
#
#     scraped_at: Optional[datetime] = None

@dataclass
class ScrapeObjectMediaDTO:
    photos: List[str] = field(default_factory=list)
    videos: List[str] = field(default_factory=list)
    

