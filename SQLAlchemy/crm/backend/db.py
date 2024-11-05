from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///crm.db", echo=True)

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    is_active = Column(Boolean, default=True)
    tasks = relationship('Task', back_populates='user')
    referred_customers = relationship('Customer', back_populates='user')


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    is_active = Column(Boolean, default=True)
    slug = Column(String, unique=True, index=True)
    tasks = relationship("Task", back_populates="category")


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    company_name = Column(String)
    email_address = Column(String)
    phone_number = Column(String)
    address = Column(String)
    comments = Column(String)
    referred_by = relationship('User', back_populates='customers', uselist=True)
    referred_id = ForeignKey(User.id)


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    creation_date = DateTime(timezone=True)
    user = relationship('User', back_populates='tasks')


if __name__ == '__main__':
    Base.metadata.create_all(engine)
