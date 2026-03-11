from dataclasses import dataclass
from fractions import Fraction
from typing import Optional


@dataclass
class CountInfo:
    text: Optional[str] = None
    count: Optional[Fraction | float | int] = None
