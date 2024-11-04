from SQLAlchemy.crm.backend.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    slug = Column(String, unique=True, index=True)
    tasks = relationship("Task", back_populates="category")
