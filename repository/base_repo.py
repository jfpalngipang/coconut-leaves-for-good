from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy.exc import IntegrityError

from sqlalchemy.orm import Session

class BaseRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]], model) -> None:
        self.session_factory = session_factory
        self.model = model

    def read_with_options(self, schema):
        with self.session_factory() as session:
            schema_dict = schema.dict(exclude_none=True)

    def read_by_id(self, id: int):
        with self.session_factory as session:
            query = session.query(self.model)
            query = query.filter(self.model.id == id).first()
            if not query:
                raise NotFoundError(detail=f"not found id : {id}")
            return query
    def create(self, schema):
        with self.session_factory as session:
            query = self.model(**schema.dict)
            try:
                session.add(query)
                session.commit()
                session.refresh(query)
            except IntegrityError as e:
                raise DuplicatedError(detail=str(e.orig))
            return query

