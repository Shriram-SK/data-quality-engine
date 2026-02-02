from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class ValidationResult:
    rule_name: str
    column: Optional[str]
    passed: bool
    severity: str 
    message: str
    invalid_count: int = 0
    total_count: int = 0
    sample_invalid_values: Optional[Any] = None
