from fastapi import APIRouter, HTTPException
from models import *
from schemas import Status
from schemas import Task_Pydantic
from schemas import TaskIn_Pydantic

router = APIRouter(prefix='/tasks', tags=['task'])


@router.get("/all_tasks")
async def get_tasks():
    return await Task_Pydantic.from_queryset(Task.all())


@router.post("/create_task")
async def create_task(task: Task_Pydantic):
    task_obj = await Task.create(**task.model_dump(exclude_unset=True))
    return await Task_Pydantic.from_tortoise_orm(task_obj)


@router.put("/update_task")
async def update_task(task_id: int, task: TaskIn_Pydantic):
    await Task.filter(id=task_id).update(**task.model_dump(exclude_unset=True))
    return await TaskIn_Pydantic.from_queryset_single(Customer.get(id=task_id))


@router.delete("/delete_task")
async def delete_task(task_id: int):
    deleted_count = await Task.filter(id=task_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    return Status(message=f"Deleted task {task_id}")
