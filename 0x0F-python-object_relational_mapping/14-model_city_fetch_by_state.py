#!/usr/bin/python3
"""
prints all the City objects from the given database
"""
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


if __name__ == "__main__":
    uname = argv[1]
    pswd = argv[2]
    db = argv[3]
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(uname, pswd, db)
    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    res = session.query(City).order_by(City.id.asc()).all()
    for row in res:
        my_query = session.query(State).filter(State.id == row.state_id)
        state_name = my_query.first().name
        print(f"{state_name}: ({row.id}) {row.name}")
