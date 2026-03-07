from dataclasses import dataclass
from fractions import Fraction
from typing import Optional


@dataclass
class AreaInfoDTO:
    text: Optional[str] = None
    amount: Optional[int | Fraction] = None
