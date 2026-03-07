from dataclasses import dataclass, field
from email.headerregistry import Address
from enum import Enum
from fractions import Fraction
from typing import Optional, List

from common import ScrapeObjectInfoDTO, ScrapeObjectMediaDTO
from prime.area import AreaInfoDTO
from prime.geo.geo_coordinates import GeoCoordinates
from prime.price.dto import PriceInfo


class RentPeriod(Enum):
    Week = 'week'
    Month = 'month'
    Year = 'year'
    
    def __str__(self) -> str:
        return self.value.__str__()


@dataclass
class PropertyFeatures:
    balcony: Optional[bool] = None
    terrace: Optional[bool] = None
    garden: Optional[bool] = None
    parking: Optional[bool] = None
    garage: Optional[bool] = None
    elevator: Optional[bool] = None
    pool: Optional[bool] = None
    
    heating: Optional[bool] = None
    heating_type: Optional[str] = None
    
    air_conditioning: Optional[bool] = None
    furnished: Optional[bool] = None
    
    energy_class: Optional[str] = None


@dataclass
class RealEstateListingDTO:
    object_info: ScrapeObjectInfoDTO = field(default_factory=ScrapeObjectInfoDTO)
    
    title: Optional[str] = None
    description_text: Optional[str] = None
    
    source_listing_id: Optional[str] = None
    multi_listing_service_id: Optional[str] = None
    
    price_primary: Optional[PriceInfo] = None
    price_secondary: Optional[PriceInfo] = None
    price_per_m2: Optional[PriceInfo] = None
    rent_period: Optional[RentPeriod | str] = None  # month, week, year
    deposit: Optional[PriceInfo] = None
    
    living_area_sq_m: Optional[AreaInfoDTO] = None
    living_area_sq_ft: Optional[AreaInfoDTO] = None
    plot_area_sq_m: Optional[AreaInfoDTO] = None
    plot_area_sq_ha: Optional[AreaInfoDTO] = None
    
    rooms: Optional[int | Fraction] = None
    bedrooms: Optional[int | Fraction] = None
    bathrooms: Optional[int | Fraction] = None
    floors_total: Optional[int | Fraction] = None
    floor_number: Optional[int | Fraction] = None
    
    features: PropertyFeatures = field(default_factory=PropertyFeatures)
    
    address: Address = field(default_factory=Address)
    geo_coordinates: Optional[GeoCoordinates] = None
    
    under_construction: Optional[bool] = None
    primary_market: Optional[bool] = None
    secondary_market: Optional[bool] = None
    renovation_needed: Optional[bool] = None
    building_type: Optional[str] = None  # apartment, house, villa etc
    building_year: Optional[int] = None
    construction_materials: Optional[List[str]] = field(default_factory=list)
    
    media: ScrapeObjectMediaDTO = field(default_factory=ScrapeObjectMediaDTO)
