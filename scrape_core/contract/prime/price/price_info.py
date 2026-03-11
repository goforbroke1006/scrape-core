from dataclasses import dataclass
from typing import Optional
from fractions import Fraction

from scrape_core.contract.prime.currency.currency_code import Currency3Code


@dataclass
class PriceInfo:
    text: Optional[str] = None
    amount: Optional[Fraction | float | int] = None
    currency: Optional[str | Currency3Code] = None
    
    def is_empty(self) -> bool:
        return (self.text is None or self.text == "") \
            and (self.amount is None or self.amount == 0)
