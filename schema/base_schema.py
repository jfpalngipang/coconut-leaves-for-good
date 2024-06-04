from datetime import datetime
from typing import List, Optional, Union

from pydantic import BaseModel


class ModelBaseInfo(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

class GetBase(BaseModel):
    ordering: Optional[str]

class GetResult(BaseModel):
    result: List