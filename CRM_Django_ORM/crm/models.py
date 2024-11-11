from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Now


class Category(models.Model):
    issue_type = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.issue_type


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30, default='Not found')
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    comments = models.TextField()
    referred_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    creation_date = models.DateTimeField(db_default=Now())
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, to_field='issue_type')

    def __str__(self):
        return self.name
