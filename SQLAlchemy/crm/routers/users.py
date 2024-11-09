from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from backend.models import User
from sqlalchemy import insert, select, update, delete
from schemas import RegisterUser

router = APIRouter(prefix='/users', tags=['user'])

@router.get("/all_users")
async def get_all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User).where(User.id)).all()
    return users

@router.post("/create_user")
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: RegisterUser):
    db.execute(insert(User).values(username=create_user.username,
                                   password=create_user.password,
                                   first_name=create_user.first_name,
                                   last_name=create_user.last_name,
                                   is_active=create_user.is_active))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }

@router.put("/update_user")
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user: RegisterUser):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no category found'
        )

    db.execute(update(User).where(User.id == user_id).values(
        username=update_user.username,
        password=update_user.password,
        first_name=update_user.first_name,
        last_name=update_user.last_name,
        is_active=update_user.is_active
    ))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Category update is successful'
    }

@router.delete("/delete_user")
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no category found'
        )
    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Category delete is successful'
    }
