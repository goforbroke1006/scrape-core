from enum import Enum

class SalaryPeriod(Enum):
    ANNUAL = 'annual'
    MONTHLY = 'monthly'
    DAILY = 'daily'
    HOURLY = 'hourly'
    
    def __str__(self) -> str:
        return self.value