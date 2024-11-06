from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///crm.db", echo=True)

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass

# if __name__ == '__main__':
#     Base.metadata.create_all(engine)
