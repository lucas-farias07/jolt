from dataclasses import dataclass
from datetime import date
from .enums.status import Status
from .base import BaseModel

@dataclass
class Task(BaseModel):
    id: int | None = None
    description: str = ""
    status: Status = Status.TODO
    deadline: date = date.min
