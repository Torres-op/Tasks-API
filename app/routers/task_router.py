from fastapi import APIRouter, status
from schemas.task_schema import Task, TaskUpdate
from services.task_service import *

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(task: Task):
    return create_task_service(task)

@router.get("/")
def list_tasks():
    return get_all_tasks_service()

@router.get("/{task_id}")
def get_task(task_id: str):
    return get_task_by_id_service(task_id)

@router.put("/{task_id}")
def update_task(task_id: str, task: Task):
    return update_task_service(task_id, task)

@router.patch("/{task_id}")
def patch_task(task_id: str, task: TaskUpdate):
    return update_task_service(task_id, task)

@router.delete("/{task_id}")
def delete_task(task_id: str):
    return delete_task_service(task_id)
