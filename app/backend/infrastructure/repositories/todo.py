from sqlalchemy import select, insert, update, delete
from typing import Any

from ...domain.models.task_model import Task
from ..database.database import DbContext, DbFunctions
from ..database.schemas import tasks_table



class ToDoRepository:
    def __init__(self) -> None:
        self.__context = DbContext()

    def select_all(self):
        with self.__context.connect() as conn:
            query = select(tasks_table)
            result: list[Task] = DbFunctions.map_to(Task, conn.execute(query))

        return result

    def insert(self, obj: Task):
        with self.__context.transaction() as conn:
            query = insert(tasks_table).values(
                description=obj.description,
                status=obj.status.value if hasattr(obj.status, "value") else obj.status,
                deadline=obj.deadline,
            )
            result = conn.execute(query)
            pk = result.inserted_primary_key

            if pk is None or len(pk) == 0:
                raise RuntimeError

            obj.id = pk[0]
            return obj

    def delete(self, task_id: int):
        with self.__context.transaction() as conn:
            query = delete(tasks_table).where(tasks_table.c.id == task_id)
            res = conn.execute(query)
            return res.rowcount > 0

    def update(self, task_id: int, values: dict[str, Any]) -> bool:
        with self.__context.transaction() as conn:
                    query = update(tasks_table).where(tasks_table.c.id == task_id).values(**values)
                    result = conn.execute(query)
                    return result.rowcount > 0
