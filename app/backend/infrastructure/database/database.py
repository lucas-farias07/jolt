from typing import Any, override

from sqlalchemy import Engine, MetaData, Row, create_engine
from sqlalchemy.engine import CursorResult

from ...config import configuration


class DbContext:
    def __init__(self) -> None:
        self.__engine: Engine = create_engine(
            f"sqlite:///{configuration['DBConnection']}", echo=True
        )
        self.metadata: MetaData = MetaData()

    @override
    def __repr__(self) -> str:
        try:
            with self.__engine.connect():
                return f"<Database status='up' url='{self.__engine.url}'>"
        except Exception as e:
            return f"<Database status='down' error='{str(e)}'>"


class DbFunctions:
    @staticmethod
    def map_to(type: type, obj: CursorResult[Any]) -> list[Any]:
        return [type(**row._mapping) for row in obj]
