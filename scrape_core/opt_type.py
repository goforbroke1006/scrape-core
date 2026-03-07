from enum import Enum


class OptionalType(Enum):
    YES = 'yes'
    NO = 'no'
    UNKNOWN = 'unknown'

    def __str__(self) -> str:
        return self.value
