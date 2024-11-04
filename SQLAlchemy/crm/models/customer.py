from SQLAlchemy.crm.backend.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Customer(Base):
    __tablename__ = 'customers'
    first_name = Column(String)
    last_name = Column(String)
    company_name = Column(String)
    email_address = Column(String)
    phone_number = Column(String)
    address = Column(String)
    comments = Column(String)
    referred_by = relationship('User', back_populates='customers', uselist=True)
