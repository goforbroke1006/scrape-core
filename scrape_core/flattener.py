from dataclasses import is_dataclass, fields
from decimal import Decimal
from fractions import Fraction
from typing import Any, Dict, List


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


def omit_empty(source: Dict[str, Any]) -> Dict[str, Any]:
    result = {}
    
    for k, v in source.items():
        if v is None:
            continue
        if isinstance(v, str) and len(v) == 0:
            continue
        if isinstance(v, (list, dict, tuple)) and len(v) == 0:
            continue
        
        result[k] = v
    
    return result


def align_columns(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    all_keys = set()
    
    for item in items:
        for k, v in item.items():
            all_keys.add(k)
    
    for item in items:
        for req_key in all_keys:
            if req_key not in item:
                item[req_key] = None
    
    return items
