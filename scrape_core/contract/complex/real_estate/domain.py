from dataclasses import dataclass, field
from enum import Enum
from fractions import Fraction
from typing import Optional, List

from scrape_core.common import ScrapeResult
from scrape_core.contract.prime.area import AreaInfo
from scrape_core.contract.prime.geo.address import AddressInfo
from scrape_core.contract.prime.geo.geo_coordinates import GeoCoordinates
from scrape_core.contract.prime.price.price_info import PriceInfo


class DealType(Enum):
    Sale = 'sale'
    Buy = 'buy'
    Rent = 'rent'
    
    def __str__(self):
        return self.value


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
class RealEstateListing(ScrapeResult):
    deal_type: DealType = None
    
    source_listing_id: Optional[str] = None
    multi_listing_service_id: Optional[str] = None
    
    price_per_m2: Optional[PriceInfo] = None
    rent_period: Optional[RentPeriod | str] = None  # month, week, year
    deposit: Optional[PriceInfo] = None
    
    living_area_sq_m: Optional[AreaInfo] = None
    living_area_sq_ft: Optional[AreaInfo] = None
    plot_area_sq_m: Optional[AreaInfo] = None
    plot_area_sq_ha: Optional[AreaInfo] = None
    
    rooms: Optional[int | Fraction] = None
    bedrooms: Optional[int | Fraction] = None
    bathrooms: Optional[int | Fraction] = None
    floors_total: Optional[int | Fraction] = None
    floor_number: Optional[int | Fraction] = None
    
    features: PropertyFeatures = field(default_factory=PropertyFeatures)
    
    address: AddressInfo = field(default_factory=AddressInfo)
    geo_coordinates: Optional[GeoCoordinates] = None
    
    under_construction: Optional[bool] = None
    primary_market: Optional[bool] = None
    secondary_market: Optional[bool] = None
    renovation_needed: Optional[bool] = None
    building_type: Optional[str] = None  # apartment, house, villa etc
    building_year: Optional[int] = None
    construction_materials: Optional[List[str]] = field(default_factory=list)
