from typing import Optional
from fractions import Fraction


class PriceInfo:
    def __init__(self, text: str, amount: Fraction, currency: Optional[str] = None):
        """Price representation with raw + normalized values"""
        self.text = text
        self.amount = amount
        self.currency = currency
