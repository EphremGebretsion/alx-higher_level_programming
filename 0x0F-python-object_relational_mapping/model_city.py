#!/usr/bin/python3
"""
module to create City that inherit from Base
that mkes it capable of ORM operation
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    City class that is mapped with cities table
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'), nullable=False)
