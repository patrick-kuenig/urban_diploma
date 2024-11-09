import datetime

from pydantic import BaseModel


class RegisterUser(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    is_active: bool


class CreateCategory(BaseModel):
    name: str
    description: str


class CreateCustomer(BaseModel):
    first_name: str
    last_name: str
    company_name: str
    email_address: str
    phone_number: str
    address: str
    comments: str
    referred_id: int


class CreateTask(BaseModel):
    name: str
    description: str
    category: int
    customer: int
    user: int
