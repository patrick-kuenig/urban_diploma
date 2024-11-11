from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from .db import Base


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    is_active = Column(Boolean, default=True)

    def __str__(self):
        return self.username


class Category(Base):
    __tablename__ = 'Category'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)
    is_active = Column(Boolean, default=True)
    slug = Column(String, unique=True, index=True)

    def __str__(self):
        return self.name


class Customer(Base):
    __tablename__ = 'Customer'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    company_name = Column(String)
    email_address = Column(String)
    phone_number = Column(String)
    address = Column(String)
    comments = Column(String)
    referred_id = Column(ForeignKey('User.id', onupdate='CASCADE', ondelete='SET NULL'), nullable=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Task(Base):
    __tablename__ = 'Task'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    creation_date = Column(DateTime, default=datetime.utcnow)
    user_id = Column(ForeignKey('User.id', onupdate='CASCADE', ondelete='SET NULL'), nullable=True)
    category_id = Column(ForeignKey('Category.id', onupdate='CASCADE', ondelete='CASCADE'))
    customer_id = Column(ForeignKey('Customer.id', onupdate='CASCADE', ondelete='CASCADE'))

    def __str__(self):
        return self.name
