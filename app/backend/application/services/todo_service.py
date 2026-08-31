from .models import Task

class ToDoService:
    def __init__(self):
        pass

    def get_tasks(self, filter_status: bool | None = None) -> list[Task]:
        if filter_status is not None:
            match filter_status:
                case True:
                    pass
                case False:
                    pass
        return []
