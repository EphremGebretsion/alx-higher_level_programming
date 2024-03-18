#!/usr/bin/python3
"""
updates State objects name to 'New Mexico' with id 2 of the
database hbtn_0e_6_usa
"""
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    uname = argv[1]
    pswd = argv[2]
    db = argv[3]
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(uname, pswd, db)
    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    row = session.query(State).filter(State.id == 2).first()
    if row:
        row.name = "New Mexico"
    session.commit()
