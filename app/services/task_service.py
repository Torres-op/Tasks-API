from repositories.task_repository import *
from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException, status

def _format_task(task):
    task["_id"] = str(task["_id"])
    return task

def _validate_id(task_id):
    try:
        ObjectId(task_id)
    except (InvalidId, Exception):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"ID inválido: '{task_id}'"
        )

def create_task_service(task):
    result = create_task(task.model_dump())
    return {"message": "Tarefa criada com sucesso", "id": str(result.inserted_id)}

def get_all_tasks_service():
    tasks = get_all_tasks()
    return [_format_task(task) for task in tasks]

def get_task_by_id_service(task_id):
    _validate_id(task_id)
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada"
        )
    return _format_task(task)

def update_task_service(task_id, task):
    _validate_id(task_id)
    update_data = {key: value for key, value in task.model_dump().items() if value is not None}
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nenhum campo fornecido para atualização"
        )
    result = update_task(task_id, update_data)
    if result.matched_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada"
        )
    return {"message": "Tarefa atualizada com sucesso"}

def delete_task_service(task_id):
    _validate_id(task_id)
    result = delete_task(task_id)
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada"
        )
    return {"message": "Tarefa deletada com sucesso"}
