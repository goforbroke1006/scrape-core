from dataclasses import is_dataclass, fields
from fractions import Fraction
from decimal import Decimal
from typing import Any


def to_json_scalar(v: Any) -> Any:
    if v is None:
        return None
    
    if isinstance(v, (str, int, float, bool)):
        return v
    
    if isinstance(v, (Fraction, Decimal)):
        return float(v)
    
    if isinstance(v, list):
        return [to_json_scalar(i) for i in v]
    
    return str(v)


def flatten_dataclass(obj: Any, prefix: str = "") -> dict:
    result = {}
    
    if not is_dataclass(obj):
        raise TypeError("Expected dataclass")
    
    for f in fields(obj):
        
        value = getattr(obj, f.name)
        key = f"{prefix}{f.name}"
        
        if is_dataclass(value):
            result.update(flatten_dataclass(value, key + "_"))
        else:
            result[key] = to_json_scalar(value)
    
    return result