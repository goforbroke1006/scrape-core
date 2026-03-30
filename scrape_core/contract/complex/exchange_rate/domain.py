from dataclasses import dataclass, field
from fractions import Fraction
from typing import Optional

from scrape_core.common import StrictTypes
from scrape_core.contract.prime.country_code.country_code import CountryAlpha2Code
from scrape_core.contract.prime.currency.currency_code import Currency3Code
from scrape_core.contract.prime.datetime import DateTimeInfo


@dataclass
class ExchangeRateRow(StrictTypes):
    provider: Optional[str] = None
    
    updated_at: DateTimeInfo = field(default_factory=DateTimeInfo)
    
    country: Optional[CountryAlpha2Code] = None
    
    system_name: Optional[str] = None
    
    base_currency: Optional[Currency3Code] = None
    quote_currency: Optional[Currency3Code] = None
    
    system_buy_rate: Optional[Fraction] = None
    system_sell_rate: Optional[Fraction] = None
    
    change_absolute: Optional[Fraction] = None
    change_percentage: Optional[Fraction] = None
