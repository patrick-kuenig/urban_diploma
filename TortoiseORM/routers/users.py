from fastapi import APIRouter, HTTPException
from models import *
from schemas import Status
from schemas import User_Pydantic
from schemas import UserIn_Pydantic



router = APIRouter(prefix='/users', tags=['user'])

@router.get("/all_users")
async def get_users():
    return await User_Pydantic.from_queryset(User.all())

@router.post("/create_user")
async def create_user(user: UserIn_Pydantic):
    user = await User.create(**user.model_dump(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user)

@router.put("/update_user")
async def update_user(user_id: int, user: UserIn_Pydantic):
    await User.filter(id=user_id).update(**user.model_dump(exclude_unset=True))
    return await User_Pydantic.from_queryset_single(User.get(id=user_id))

@router.delete("/delete_user")
async def delete_user(user_id: int):
    deleted_count = await User.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return Status(message=f"Deleted user {user_id}")
