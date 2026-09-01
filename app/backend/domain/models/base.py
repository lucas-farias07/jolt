from dataclasses import dataclass, asdict
from datetime import date, datetime
from enum import Enum
from typing import Any


@dataclass
class BaseModel:
    def to_dict(self) -> dict[str, Any]:
        def serialize(value):
            if isinstance(value, Enum):
                return value.value
            if isinstance(value, (date, datetime)):
                return value.isoformat()
            if isinstance(value, list):
                return [serialize(item) for item in value]
            if isinstance(value, dict):
                return {k: serialize(v) for k, v in value.items()}
            return value

        return {k: serialize(v) for k, v in asdict(self).items()}
