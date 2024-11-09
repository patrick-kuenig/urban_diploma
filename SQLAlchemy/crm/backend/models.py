from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from .db import Base


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    is_active = Column(Boolean, default=True)
    tasks = relationship('Task', back_populates='user')
    referred_customers = relationship('Customer', back_populates='referring_user')


class Category(Base):
    __tablename__ = 'Category'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)
    is_active = Column(Boolean, default=True)
    slug = Column(String, unique=True, index=True)
    tasks = relationship('Task', back_populates='category')


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
    referred_id = ForeignKey('User.id')
    referring_user = relationship('User', back_populates='referred_customers')
    tasks = relationship('Task', back_populates='customer')


class Task(Base):
    __tablename__ = 'Task'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    creation_date = DateTime(timezone=True)
    user_id = ForeignKey('User.id')
    category_id = ForeignKey('Category.id')
    customer_id = ForeignKey('Customer.id')
    category = relationship('Category', back_populates='tasks')
    user = relationship('User', back_populates='tasks')
    customer = relationship('Customer', back_populates='tasks')
