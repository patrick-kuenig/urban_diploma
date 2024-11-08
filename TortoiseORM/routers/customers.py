from fastapi import APIRouter, HTTPException
from models import *
from schemas import Status
from schemas import Customer_Pydantic
from schemas import CustomerIn_Pydantic

router = APIRouter(prefix='/customers', tags=['customer'])


@router.get("/all_customers")
async def get_customers():
    return await Customer_Pydantic.from_queryset(Customer.all())


@router.post("/create_customer")
async def create_customer(customer: Customer_Pydantic):
    customer_obj = await Customer.create(**customer.model_dump(exclude_unset=True))
    return await Customer_Pydantic.from_tortoise_orm(customer_obj)


@router.put("/update_customer")
async def update_customer(customer_id: int, customer: CustomerIn_Pydantic):
    await Customer.filter(id=customer_id).update(**customer.model_dump(exclude_unset=True))
    return await CustomerIn_Pydantic.from_queryset_single(Customer.get(id=customer_id))


@router.delete("/delete_customer")
async def delete_customer(customer_id: int):
    deleted_count = await Customer.filter(id=customer_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Customer {customer_id} not found")
    return Status(message=f"Deleted customer {customer_id}")
