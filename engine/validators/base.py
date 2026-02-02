from abc import ABC, abstractmethod
from engine.core.result import ValidationResult


class BaseValidator(ABC):

    def __init__(self, rule_config: dict):
        self.rule_config = rule_config

    @abstractmethod
    def validate(self, dataset) -> ValidationResult:
        pass
