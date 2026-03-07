from dataclasses import dataclass, field
from datetime import datetime
from fractions import Fraction
from typing import Dict, Tuple, Any, Optional, List


@dataclass
class ScrapeObjectInfoDTO:
    """Information about the website where the listing was found"""
    domain: Optional[str] = None
    details_url: Optional[str] = None
    
    scraped_at: Optional[datetime] = None

@dataclass
class ScrapeObjectMediaDTO:
    photos: List[str] = field(default_factory=list)
    videos: List[str] = field(default_factory=list)
    

