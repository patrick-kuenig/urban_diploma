from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(primary_key=True)
    username = fields.CharField(max_length=30, unique=True)
    password = fields.CharField(max_length=50)
    first_name = fields.CharField(max_length=30)
    last_name = fields.CharField(max_length=30)
    is_active = fields.BooleanField(default=True)

    def __str__(self):
        return self.username


class Customer(Model):
    id = fields.IntField(primary_key=True)
    first_name = fields.CharField(max_length=30)
    last_name = fields.CharField(max_length=30)
    company_name = fields.CharField(max_length=30)
    email_address = fields.CharField(max_length=30)
    phone_number = fields.CharField(max_length=30)
    address = fields.CharField(max_length=50)
    comments = fields.TextField()
    referred_by = fields.ForeignKeyField('User')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=30)
    description = fields.TextField()

    def __str__(self):
        return self.name


class Task(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=50)
    description = fields.TextField()
    creation_date = fields.DatetimeField(auto_now_add=True)
    user = fields.ForeignKeyField('User')
    category = fields.ForeignKeyField('Category')
    customer = fields.ForeignKeyField('Customer')

    def __str__(self):
        return self.name
