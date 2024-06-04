from sqlmodel import Field, JSON, DateTime
from base import BaseModel

class ClusteredAlerts(BaseModel, table=True):
    id: str = Field(nullable=False)
    user_id: str = Field(nullable=False)
    priority: str = Field(nullable=False)
    email: str = Field(nullable=False)
    date_from: DateTime = Field(nullable=False)
    date_to: DateTime = Field(nullable=False)
