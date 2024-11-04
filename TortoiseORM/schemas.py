from pydantic import BaseModel

class RegisterUser(BaseModel):
    username = str
    password = str
    first_name = str
    last_name = str


class CreateCategory(BaseModel):
    name: str
    description = str
    parent_id = int


class Customer(BaseModel):
    pass
