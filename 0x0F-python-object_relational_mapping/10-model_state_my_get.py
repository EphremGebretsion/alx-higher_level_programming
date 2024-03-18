#!/usr/bin/python3
"""
searchs for State objects by name from the database hbtn_0e_6_usa
and displays id or Not found
"""
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    uname = argv[1]
    pswd = argv[2]
    db = argv[3]
    search_name = argv[4]
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(uname, pswd, db)
    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    row = session.query(State).filter(State.name == search_name).first()
    if row:
        print(row.id)
    else:
        print("Not found")
