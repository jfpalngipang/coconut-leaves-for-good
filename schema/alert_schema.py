from pydantic import BaseModel
from schema.base_schema import FindBase
# from util.schema import AllOptional

class BaseAlert(BaseModel):
    alert_rule_id: int
    alert_rule_name: str
    user_id: str
    email: str
    transaction_id: str

    class Config:
        orm_mode = True

class Alert(ModelBaseInfo, BaseAlert): ...

class GetAlerts(GetBase, BaseAlert): ...

class GetAlertsResult(BaseModel):
    result: List[Alert]