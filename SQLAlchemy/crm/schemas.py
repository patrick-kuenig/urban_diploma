from pydantic import BaseModel


class RegisterUser(BaseModel):
    username = str
    password = str
    first_name = str
    last_name = str


class CreateCategory(BaseModel):
    name: str
    description = str


class CreateCustomer(BaseModel):
    first_name: str
    last_name: str
    company_name: str
    email_address: str
    phone_number: str
    address: str
    comments: str
    referred_by: int | None

class Task(BaseModel):
    name: str
    description: str
    creation_date: str
    user: int | None
    customer: int | None

