from dataclasses import dataclass, field
from fractions import Fraction
from typing import Optional

from scrape_core.common import ScrapeResult
from scrape_core.contract.prime.count_info import CountInfo
from scrape_core.contract.prime.country_code.country_code import CountryAlpha2Code


@dataclass
class ProductBrandInfo:
    brand_name: Optional[str] = None
    manufacturer_name: Optional[str] = None
    manufacturer_country: Optional[CountryAlpha2Code] = None
    importer_name: Optional[str] = None
    importer_country: Optional[CountryAlpha2Code] = None


@dataclass
class ProductBarcodeInfo:
    ean13: Optional[str] = None
    upc: Optional[str] = None
    sku: Optional[str] = None
    internal_id: Optional[str] = None


@dataclass
class ComputingCharacteristics:
    motherboard_model: Optional[str] = None
    cpu_model: Optional[str] = None
    cpu_count: Optional[int] = None
    ram_model: Optional[str] = None
    ram_volume_gb: Optional[int | Fraction] = None
    gpu_model: Optional[str] = None
    gpu_volume_gb: Optional[int | Fraction] = None


@dataclass
class ProductAvailability:
    in_stock: Optional[bool] = None
    stock_quantity: CountInfo = field(default_factory=CountInfo)


@dataclass
class ProductListing(ScrapeResult):
    internal_id: Optional[str] = None
    
    brand_info: ProductBrandInfo = field(default_factory=ProductBrandInfo)
    barcode_info: ProductBarcodeInfo = field(default_factory=ProductBarcodeInfo)
    computing_characteristics: ComputingCharacteristics = field(default_factory=ComputingCharacteristics)
    availability: ProductAvailability = field(default_factory=ProductAvailability)
