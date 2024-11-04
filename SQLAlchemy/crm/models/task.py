from SQLAlchemy.crm.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    creation_date = DateTime(timezone=True)
    user = relationship('User', back_populates='tasks')