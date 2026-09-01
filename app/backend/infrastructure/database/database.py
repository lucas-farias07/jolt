from typing import Any, override

from sqlalchemy import Engine, MetaData, Row, create_engine
from sqlalchemy.engine import Connection, CursorResult

from .schemas import metadata
from ...config import configuration, ROOT_DIR

import contextlib
from typing import Iterator

class DbContext:
    def __init__(self) -> None:
        self.engine: Engine = create_engine(
            f"sqlite:///{str(ROOT_DIR / configuration['DBConnection'])}", echo=True
        )
        self.metadata: MetaData = metadata
        self.metadata.create_all(self.engine)

    @contextlib.contextmanager
    def connect(self) -> Iterator[Connection]:
        with self.engine.connect() as conn:
            yield conn

    @contextlib.contextmanager
    def transaction(self) -> Iterator[Connection]:
        with self.engine.begin() as conn:
            yield conn

    @override
    def __repr__(self) -> str:
        try:
            with self.engine.connect():
                return f"<Database status='up' url='{self.engine.url}'>"
        except Exception as e:
            return f"<Database status='down' error='{str(e)}'>"


class DbFunctions:
    @staticmethod
    def map_to(type_obj: type, obj: CursorResult[Any]) -> list[Any]:
        return [type_obj(**row._mapping) for row in obj]
