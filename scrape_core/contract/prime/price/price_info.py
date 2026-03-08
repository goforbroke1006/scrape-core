from dataclasses import dataclass
from typing import Optional
from fractions import Fraction

from scrape_core.contract.prime.currency.currency_code import Currency3Code


@dataclass
class PriceInfo:
    text: Optional[str] = None
    amount: Optional[Fraction | float | int] = None
    currency: Optional[str | Currency3Code] = None
