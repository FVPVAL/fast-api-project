from sqlalchemy import create_engine, DateTime, func
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./staff.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

Base = declarative_base()


class Person(Base):
    __tablename__ = "staff"
    id = Column(Integer, primary_key=True, index=True)
    surname = Column(String)
    name = Column(String)
    salary = Column(Integer)
    date = Column(DateTime, server_default=func.now())


SessionLocal = sessionmaker(autoflush=False, bind=engine)
