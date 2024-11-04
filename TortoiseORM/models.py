from tortoise.models import Model
from tortoise import fields

# __models__ = ['User', 'Customer', 'Task', 'Category']


class User(Model):
    id = fields.IntField(primary_key=True)
    username = fields.CharField(max_length=30)
    password = fields.CharField(max_length=50)
    first_name = fields.CharField(max_length=30)
    last_name = fields.CharField(max_length=30)
    is_active = fields.BooleanField(default=True)

    def __str__(self):
        return self.username


class Customer(Model):
    first_name = fields.CharField(max_length=30)
    last_name = fields.CharField(max_length=30)
    company_name = fields.CharField(max_length=30)
    email_address = fields.CharField(max_length=30)
    phone_number = fields.CharField(max_length=30)
    address = fields.CharField(max_length=50)
    comments = fields.TextField()
    referred_by = fields.ForeignKeyField('models.User', related_name='customers')


class Task(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=50)
    description = fields.TextField()
    creation_date = fields.DatetimeField(auto_now_add=True)
    user = fields.ForeignKeyField('models.User', related_name='tasks')


class Category(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=30)
