#!/usr/bin/python3
"""
module for defining State and Base
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sys import argv


url = "mysql+mysqldb://{uname}:{pwd}@localhost:3306/{db}".format(uname=argv[1], pwd=argv[2], db=argv[3])
engine = create_engine(url, pool_pre_ping=True)
Base = declarative_base()
class State(Base):
    """
    state class that connects with database table states
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
