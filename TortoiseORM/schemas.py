from pydantic import BaseModel
from typing import TYPE_CHECKING
from models import User, Customer, Task, Category
from tortoise.contrib.pydantic import PydanticModel, pydantic_model_creator

# if TYPE_CHECKING:
#     class UserIn_Pydantic(User, PydanticModel):
#         pass
#
#
#     class User_Pydantic(User, PydanticModel):
#         pass
#
#
#     class CustomerIn_Pydantic(Customer, PydanticModel):
#         pass
#
#
#     class Customer_Pydantic(Customer, PydanticModel):
#         pass
#
#
#     class TaskIn_Pydantic(Task, PydanticModel):
#         pass
#
#
#     class Task_Pydantic(Task, PydanticModel):
#         pass
#
#
#     class CategoryIn_Pydantic(Category, PydanticModel):
#         pass
#
#
#     class Category_Pydantic(Category, PydanticModel):
#         pass
#
# else:
User_Pydantic = pydantic_model_creator(User, name='User')
UserIn_Pydantic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)

Customer_Pydantic = pydantic_model_creator(Customer, name='Customer')
CustomerIn_Pydantic = pydantic_model_creator(Customer, name='CustomerIn', exclude_readonly=True)

Task_Pydantic = pydantic_model_creator(Task, name='Task')
TaskIn_Pydantic = pydantic_model_creator(Task, name='TaskIn', exclude_readonly=True)

Category_Pydantic = pydantic_model_creator(Category, name='Task')
CategoryIn_Pydantic = pydantic_model_creator(Category, name='TaskIn', exclude_readonly=True)


class Status(BaseModel):
    message: str