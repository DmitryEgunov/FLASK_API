from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from db import engine

Base = declarative_base(bind=engine)


class AnAd(Base):

    __tablename__ = 'ads'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), nullable=False)
    description = Column(String, nullable=False)
    creation_date = Column(DateTime, server_default=func.now())
    owner = Column(String(30), nullable=False, index=True)


Base.metadata.create_all()