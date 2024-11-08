from fastapi import APIRouter, HTTPException
from models import *
from schemas import Status
from schemas import CategoryIn_Pydantic
from schemas import Category_Pydantic

router = APIRouter(prefix='/categories', tags=['category'])


@router.get("/all_categories")
async def get_categories():
    return await Category_Pydantic.from_queryset(User.all())


@router.post("/create_category")
async def create_category(category: Category_Pydantic):
    category = await Category.create(**category.model_dump(exclude_unset=True))
    return await Category_Pydantic.from_tortoise_orm(category)


@router.put("/update_category")
async def update_category(category_id: int, category: CategoryIn_Pydantic):
    await Category.filter(id=category_id).update(**category.model_dump(exclude_unset=True))
    return await CategoryIn_Pydantic.from_queryset_single(User.get(id=category_id))


@router.delete("/delete_category")
async def delete_category(category_id: int):
    deleted_count = await Category.filter(id=category_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Category {category_id} not found")
    return Status(message=f"Deleted category {category_id}")
