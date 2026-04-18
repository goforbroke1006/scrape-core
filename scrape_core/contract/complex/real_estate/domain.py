from dataclasses import dataclass, field
from enum import Enum
from fractions import Fraction
from typing import Optional, List

from scrape_core.common import ScrapeResult
from scrape_core.contract.prime.area import AreaInfo
from scrape_core.contract.prime.count_info import CountInfo
from scrape_core.contract.prime.datetime import DateTimeInfo
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
    Day = 'day'
    Week = 'week'
    Month = 'month'
    Year = 'year'
    
    def __str__(self) -> str:
        return self.value.__str__()


@dataclass
class PropertyFeatures:
    amenities_list: List[str] = field(default_factory=list)
    
    storage_room: Optional[bool] = None
    balcony: Optional[bool] = None
    terrace: Optional[bool] = None
    terrace_area_sq_m: AreaInfo = field(default_factory=AreaInfo)
    garden: Optional[bool] = None
    parking: Optional[bool] = None
    parking_spaces: CountInfo = field(default_factory=CountInfo)
    covered_parking: Optional[bool] = None
    garage: Optional[bool] = None
    elevator: Optional[bool] = None
    pool: Optional[bool] = None
    
    heating: Optional[bool] = None
    heating_type: Optional[str] = None
    
    air_conditioning: Optional[bool] = None
    furnished: Optional[bool] = None
    
    energy_class: Optional[str] = None


@dataclass
class LocationFeatures:
    distance_to_center_meters: CountInfo = field(default_factory=CountInfo)
    distance_to_sea_meters: CountInfo = field(default_factory=CountInfo)
    distance_to_metro_meters: CountInfo = field(default_factory=CountInfo)
    duration_to_metro_minutes: CountInfo = field(default_factory=CountInfo)  # TODO: walking or on a car
    metro_stations: List[str] = field(default_factory=list)


@dataclass
class RentConditions:
    available_from_date: DateTimeInfo = field(default_factory=DateTimeInfo)
    from_date: DateTimeInfo = field(default_factory=DateTimeInfo)
    till_date: DateTimeInfo = field(default_factory=DateTimeInfo)
    guests_count_max: CountInfo = field(default_factory=CountInfo)
    payment_period: Optional[RentPeriod] = None  # month, week, year
    is_owner: Optional[bool] = None
    commission: PriceInfo = field(default_factory=PriceInfo)
    deposit: PriceInfo = field(default_factory=PriceInfo)
    no_pets: Optional[bool] = None
    
    per_year: PriceInfo = field(default_factory=PriceInfo)


@dataclass
class RealEstateListing(ScrapeResult):
    deal_type: DealType = None
    
    source_listing_id: Optional[str | int] = None
    multi_listing_service_id: Optional[str] = None
    
    property_type: Optional[str] = None
    
    price_per_m2: PriceInfo = field(default_factory=PriceInfo)
    
    rent_conditions: RentConditions = field(default_factory=RentConditions)
    
    living_area_sq_m: AreaInfo = field(default_factory=AreaInfo)
    living_area_sq_ft: AreaInfo = field(default_factory=AreaInfo)
    plot_area_sq_m: AreaInfo = field(default_factory=AreaInfo)
    plot_area_sq_ha: AreaInfo = field(default_factory=AreaInfo)
    
    rooms: CountInfo = field(default_factory=CountInfo)
    bedrooms: CountInfo = field(default_factory=CountInfo)
    bathrooms: CountInfo = field(default_factory=CountInfo)
    receptions: CountInfo = field(default_factory=CountInfo)
    floors_total: Optional[int | Fraction] = None
    floor_number: Optional[int | Fraction] = None
    
    property_features: PropertyFeatures = field(default_factory=PropertyFeatures)
    location_features: LocationFeatures = field(default_factory=LocationFeatures)
    
    address: AddressInfo = field(default_factory=AddressInfo)
    geo_coordinates: Optional[GeoCoordinates] = None
    
    under_construction: Optional[bool] = None
    primary_market: Optional[bool] = None
    secondary_market: Optional[bool] = None
    renovation_needed: Optional[bool] = None
    developer_name: Optional[str] = None
    
    agency_name: Optional[str] = None
    agent_name: Optional[str] = None
    
    building_type: Optional[str] = None  # apartment, house, villa etc
    building_year: Optional[int] = None
    construction_materials: List[str] = field(default_factory=list)
    
    phone_number: Optional[str] = None
