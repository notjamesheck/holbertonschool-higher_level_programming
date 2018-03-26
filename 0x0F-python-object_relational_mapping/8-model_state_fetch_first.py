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

    poop = session.query(State).first()
    if poop is None:
        ""
        ""
        print('Nothing')
    else:
        print("{}: {}".format(poop.id, poop.name))

    session.close()
