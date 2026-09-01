from datetime import date
from flask import Blueprint, jsonify, request
from ..responses import ok, err
from ....application.services.todo import ToDoService
from ....domain.models.task_model import Task


todo_bp = Blueprint("todo", __name__, url_prefix="/todo")

__todo_service = ToDoService()

# --- Get functions ---
@todo_bp.get("/tasks/<int:task_id>")
def get_task(task_id: int):
    try:
        task = __todo_service.get_task(task_id=task_id)
        if task is None:
            return err(f"No item found with id {task_id}.", 404)

        return ok(task.to_dict())
    except Exception as e:
        return err(message=f"{e}")

@todo_bp.get("/tasks")
def get_all_tasks():
    status_raw = request.args.getlist('status')
    filters = [int(s) for s in status_raw] if status_raw else []
    tasks = __todo_service.get_tasks(filters)
    return ok([task.to_dict() for task in tasks])

# --- Add and Remove ---
@todo_bp.post("/tasks/add")
def add_task():
    try:
        data = request.get_json()
        task = Task(
            deadline=date.fromisoformat(data['deadline']),
            description=data.get('description')
        )

        id = __todo_service.add_task(task)
        if id is None:
            raise IndexError("Couldn't save task.")

        return ok({"id": id})

    except Exception as e:
        return err(message=f"{e}")

@todo_bp.delete("/tasks/<int:task_id>")
def remove_task(task_id: int):
    try:
        deleted = __todo_service.remove_task(task_id)
        if not deleted:
            return err(f"No item found with id {task_id}.", 404)

        return ok({})
    except Exception as e:
        return err(message=f"{e}")

@todo_bp.patch("/tasks/<int:task_id>")
def update_task(task_id: int):
    raise NotImplementedError
    try:
        data = request.get_json()
        if not data:
            return err(f"No input provided to update.", 400)
        return ok({})
    except Exception as e:
        return err(message=f"{e}")
