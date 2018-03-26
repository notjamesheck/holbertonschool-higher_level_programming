#!/usr/bin/python3

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[0], sys.argv[1], sys.argv[2]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    session = Session(bind=engine)

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        session.close()
