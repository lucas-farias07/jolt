from typing import Any

from app.backend.infrastructure.database.schemas import tasks_table

from ...domain.models.enums.status import Status
from ...domain.models.task_model import Task
from ...infrastructure.repositories.todo import ToDoRepository


class ToDoService:
    def __init__(self):
        self.__todo_repo = ToDoRepository()

    def get_tasks(self, status_filter: list[int]) -> list[Task]:
        tasks: list[Task] = self.__todo_repo.select_all()
        if len(status_filter) != 0:
            #to allow someone to query different combinations of filters
            filters: list[Status] = [Status(status) for status in status_filter]
            #tasks that fit in the filter
            filtered_tasks: list[Task] = [task for task in tasks if task.status in filters]

            return filtered_tasks

        return tasks

    def get_task(self, task_id: int) -> Task | None:
        tasks: list[Task] = self.__todo_repo.select_all()
        #takes first item of the list. if no items, takes None as value
        task: Task | None = next((task for task in tasks if task.id == task_id), None)

        return task

    def add_task(self, task: Task) -> int | None:
        obj = self.__todo_repo.insert(task)
        if obj.id == None:
            raise ValueError

        return obj.id

    def remove_task(self, task_id: int) -> bool:
        res = self.__todo_repo.delete(task_id)
        return res

    def update_task(self, task_id: int, values: dict[str, Any]) -> bool:
        raise NotImplementedError
