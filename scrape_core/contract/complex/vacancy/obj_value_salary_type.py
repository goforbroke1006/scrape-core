from enum import Enum

class SalaryType(Enum):
    GROSS = 'gross'
    NET = 'net'
    
    def __str__(self) -> str:
        return self.value