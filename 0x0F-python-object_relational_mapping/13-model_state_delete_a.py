#!/usr/bin/python3

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker()
    session = Session(bind=engine)

    for poop in session.query(State).order_by(State.name):
        if 'a' in poop.name:
            borp = poop
            session.delete(borp)
            session.commit()

    session.close()
