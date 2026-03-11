import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class DateTimeInfo:
    text: Optional[str] = None
    time: Optional[datetime.date | datetime.datetime] = None
