from dataclasses import dataclass, field
from enum import Enum
from fractions import Fraction
from typing import Optional, List

from scrape_core.common import ScrapeResult
from scrape_core.contract.prime.count_info import CountInfo
from scrape_core.contract.prime.country_code.country_code import CountryAlpha2Code
from scrape_core.contract.prime.datetime import DateTimeInfo


class ProductUnit(Enum):
    Gram = "g"
    Kilogram = "kg"
    Milliliter = "ml"
    Liter = "l"
    Piece = "pcs"
    Pack = "pack"
    
    Ounce = "oz"
    Pound = "lb"
    FluidOunce = "fl oz"
    
    def __str__(self):
        return self.value


class PackagingType(Enum):
    Bottle = "bottle"
    Can = "can"
    Box = "box"
    Bag = "bag"
    Jar = "jar"
    Pack = "pack"
    Vacuum = "vacuum"
    Other = "other"
    
    def __str__(self):
        return self.value


@dataclass
class ProductBrandInfo:
    brand_name: Optional[str] = None
    manufacturer_name: Optional[str] = None
    manufacturer_country: Optional[CountryAlpha2Code] = None
    importer_name: Optional[str] = None
    importer_country: Optional[CountryAlpha2Code] = None


@dataclass
class VolumeInfo:
    text: Optional[str] = None  # per 100g / per serving
    count: Optional[Fraction | float | int] = None
    unit: Optional[ProductUnit] = None


@dataclass
class ProductSizeInfo:
    item_volume_si: VolumeInfo = field(default_factory=VolumeInfo)  # weight or volume
    item_volume_imp: VolumeInfo = field(default_factory=VolumeInfo)  # weight or volume
    pack_count: CountInfo = field(default_factory=CountInfo)  # items in pack
    total_volume: VolumeInfo = field(default_factory=VolumeInfo)


@dataclass
class ProductNutritionInfo:
    energy_kcal: CountInfo = field(default_factory=CountInfo)
    energy_kj: CountInfo = field(default_factory=CountInfo)
    
    fat_g: CountInfo = field(default_factory=CountInfo)
    fat_saturated_g: CountInfo = field(default_factory=CountInfo)
    
    carbohydrates_g: CountInfo = field(default_factory=CountInfo)
    sugar_g: CountInfo = field(default_factory=CountInfo)
    
    protein_g: CountInfo = field(default_factory=CountInfo)
    salt_g: CountInfo = field(default_factory=CountInfo)
    fiber_g: CountInfo = field(default_factory=CountInfo)
    
    per_volume: VolumeInfo = field(default_factory=VolumeInfo)


@dataclass
class ProductIngredientsInfo:
    ingredients: Optional[List[str]] = field(default_factory=list)
    allergens: Optional[List[str]] = field(default_factory=list)
    additives: Optional[List[str]] = field(default_factory=list)
    contains_palm_oil: Optional[bool] = None
    contains_gluten: Optional[bool] = None
    contains_lactose: Optional[bool] = None
    vegan: Optional[bool] = None
    vegetarian: Optional[bool] = None


@dataclass
class ProductPackagingInfo:
    packaging_type: Optional[PackagingType] = None
    recyclable: Optional[bool] = None
    material: Optional[str] = None
    weight_with_packaging_g: Optional[float] = None


@dataclass
class ProductLogisticsInfo:
    storage_conditions: Optional[str] = None
    expiration_date: DateTimeInfo = field(default_factory=DateTimeInfo)
    production_date: DateTimeInfo = field(default_factory=DateTimeInfo)


@dataclass
class ProductBarcodeInfo:
    ean13: Optional[str] = None
    upc: Optional[str] = None
    sku: Optional[str] = None
    internal_id: Optional[str] = None


@dataclass
class ProductAvailability:
    in_stock: Optional[bool] = None
    stock_quantity: CountInfo = field(default_factory=CountInfo)
    min_order_quantity: CountInfo = field(default_factory=CountInfo)
    max_order_quantity: CountInfo = field(default_factory=CountInfo)


@dataclass
class ProductCategories:
    category: Optional[str] = None
    subcategory: Optional[str] = None


@dataclass
class GroceryListing(ScrapeResult):
    brand_info: ProductBrandInfo = field(default_factory=ProductBrandInfo)
    
    size_info: ProductSizeInfo = field(default_factory=ProductSizeInfo)
    
    nutrition_info: ProductNutritionInfo = field(default_factory=ProductNutritionInfo)
    
    ingredients_info: ProductIngredientsInfo = field(default_factory=ProductIngredientsInfo)
    
    packaging_info: ProductPackagingInfo = field(default_factory=ProductPackagingInfo)
    
    logistics_info: ProductLogisticsInfo = field(default_factory=ProductLogisticsInfo)
    
    barcode_info: ProductBarcodeInfo = field(default_factory=ProductBarcodeInfo)
    
    categories: ProductCategories = field(default_factory=ProductCategories)
    
    availability: ProductAvailability = field(default_factory=ProductAvailability)
    
    tags: Optional[List[str]] = field(default_factory=list)
    
    country_of_origin: Optional[CountryAlpha2Code] = None
