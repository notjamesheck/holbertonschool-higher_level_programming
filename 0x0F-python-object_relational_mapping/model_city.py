#!/usr/bin/python3


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String


if __name__ == '__main__':
    ""
    ""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True)
    name = Column(String(128), nullable=false)
    state_id = Column(Integer, nullable=false, ForeignKey('states.id'))
