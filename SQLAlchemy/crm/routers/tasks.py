from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from backend.models import Task
from sqlalchemy import insert, select, update, delete
from schemas import CreateTask

router = APIRouter(prefix='/tasks', tags=['task'])


@router.get("/all_tasks")
async def get_all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task).where(Task.id)).all()
    return tasks


@router.post("/create_task")
async def create_task(db: Annotated[Session, Depends(get_db)], create_task: CreateTask):
    db.execute(insert(Task).values({"name": create_task.name,
                                    "description": create_task.description,
                                    "user_id": create_task.user,
                                    "category_id": create_task.category,
                                    "customer_id": create_task.customer}))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put("/update_task")
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, update_task: CreateTask):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no category found'
        )

    db.execute(update(Task).where(Task.id == task_id).values(
        ame=create_task.name,
        description=create_task.description,
        user_id=create_task.user,
        category_id=create_task.category,
        customer_id=create_task.customer))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task update was successful'
    }


@router.delete("/delete_task")
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no category found')
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task was successfully deleted'
    }
