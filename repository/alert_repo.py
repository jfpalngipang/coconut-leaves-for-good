from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy.orm import Session
from models.alert import Alert
from repository.base_repo import BaseRepository

class AlertRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, Alert)