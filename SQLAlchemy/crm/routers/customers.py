from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from SQLAlchemy.crm.backend.db_depends import get_db
from typing import Annotated
from SQLAlchemy.crm.backend.db import *
from sqlalchemy import insert, select, update, delete
from SQLAlchemy.crm.schemas import CreateCustomer

router = APIRouter(prefix='/customers', tags=['customer'])


@router.get("/all_customers")
async def get_all_customers(db: Annotated[Session, Depends(get_db)]):
    customers = db.scalars(select(Customer).where(Customer.id)).all()
    return customers


@router.post("/create")
async def create_customer(db: Annotated[Session, Depends(get_db)], customer: CreateCustomer):
    db.execute(insert(Customer).values(first_name=customer.first_name,
                                       last_name=customer.last_name,
                                       company_name=customer.company_name,
                                       email_address=customer.email_address,
                                       phone_number=customer.email_address,
                                       address=customer.address,
                                       comments=customer.comments))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put("/edit")
async def edit_customer(db: Annotated[Session, Depends(get_db)], customer_id: int, update_customer: CreateCustomer):
    customer = db.scalar(select(Customer).where(Customer.id == customer_id))
    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no category found'
        )

    db.execute(update(Customer).where(Customer.id == customer_id).values(
        first_name=update_customer.first_name,
        last_name=update_customer.last_name,
        company_name=update_customer.company_name,
        email_address=update_customer.email_address,
        phone_number=update_customer.email_address,
        address=update_customer.address,
        comments=update_customer.comments
    ))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Customer update was successful'
    }

@router.delete("/delete")
async def delete_customer(db: Annotated[Session, Depends(get_db)], customer_id: int):
    customer = db.scalar(select(Customer).where(Customer.id == customer_id))
    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no category found'
        )
    db.execute(delete(Customer).where(Customer.id == customer_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Customer deletion was successful'
    }
