from dataclasses import dataclass, field
from fractions import Fraction
from typing import List, Optional, Dict, Any

from scrape_core.common import ScrapeResult
from scrape_core.contract.prime.count_info import CountInfo
from scrape_core.contract.prime.datetime import DateTimeInfo
from scrape_core.contract.prime.geo.address import AddressInfo
from scrape_core.contract.prime.price.price_info import PriceInfo


@dataclass
class SubstanceAmount:
    text: Optional[str] = None
    amount: Optional[Fraction | int] = None


@dataclass
class VehicleListing(ScrapeResult):
    source_listing_id: Optional[str] = None
    
    vin: Optional[str] = None
    
    brand_name: Optional[str] = None
    model_name: Optional[str] = None
    trim_level: Optional[str] = None
    issue_year: Optional[int] = None
    
    body_type: Optional[str] = None  # Hatchback | SUV | Coupe | Saloon
    interior_colors: Optional[List[str]] = field(default_factory=list)
    exterior_colors: Optional[List[str]] = field(default_factory=list)
    
    transmission_type: Optional[str] = None  # Automatic | Manual
    drivetrain: Optional[str] = None  # AWD | FWD | RWD
    fuel_type: Optional[str] = None  # Petrol | Diesel | Electric
    
    horse_power: CountInfo = field(default_factory=CountInfo)
    mileage_miles: CountInfo = field(default_factory=CountInfo)
    mileage_kilometers: CountInfo = field(default_factory=CountInfo)
    engine_capacity_l: SubstanceAmount = field(default_factory=SubstanceAmount)
    engine_capacity_cc: SubstanceAmount = field(default_factory=SubstanceAmount)
    
    engine_type: Optional[str] = None
    
    condition_new: Optional[bool] = None
    condition_used: Optional[bool] = None
    
    owners: CountInfo = field(default_factory=CountInfo)
    accidents: CountInfo = field(default_factory=CountInfo)
    
    phone_number: Optional[str] = None
    
    fuel_consumption_l_per_100km: SubstanceAmount = field(default_factory=SubstanceAmount)
    miles_per_gallon_city: SubstanceAmount = field(default_factory=SubstanceAmount)
    miles_per_gallon_highway: SubstanceAmount = field(default_factory=SubstanceAmount)
    co2_emission_g_per_km: SubstanceAmount = field(default_factory=SubstanceAmount)
    
    last_service_date: DateTimeInfo = field(default_factory=DateTimeInfo)
    
    price_system_recommended: PriceInfo = field(default_factory=PriceInfo)
    
    seller_name: Optional[str] = None
    seller_location: AddressInfo = field(default_factory=AddressInfo)
    
    features_list: Optional[List[str]] = field(default_factory=list)
    features_map: Optional[Dict[str, Any]] = field(default_factory=dict)

