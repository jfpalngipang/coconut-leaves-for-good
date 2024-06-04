from sqlmodel import Field
from models.base import BaseModel

class Alert(BaseModel, table=True):
    alert_rule_id: int = Field(nullable=False)
    alert_rule_name: str = Field(nullable=False)
    user_id: str = Field(nullable=False)
    email: str = Field()
    transaction_id: str = Field()
    # related_transactions: JSON = Field()
