from sqlmodel import Field, JSON, Enum
from base import BaseModel
import enum

class Ineqs(enum.Enum):
    gte = ">="
    gt = ">"
    lte = "<="
    lt = "<"
    eq = "=="

class Units(enum.Enum):
    php = "php"
    count = "count"

class AlertRule(BaseModel, table=True):
    id: int = Field(nullable=False)
    name: str = Field(nullable=False)
    domain: str = Field(nullable=False)
    inequality: Ineqs = Field(sa_column=Column(Enum(Ineqs)))
    threshold: float = Field(nullable=False)
    unit: Units = Field(sa_column=Column(Enum(Units)))