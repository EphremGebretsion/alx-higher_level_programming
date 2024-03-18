#!/usr/bin/python3
"""
lists the first State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


uname = argv[1]
pswd = argv[2]
db = argv[3]
url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(uname, pswd, db)
engine = create_engine(url, pool_pre_ping=True)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
first_row = session.query(State).first()
if first_row:
    print(f"{first_row.id}: {first_row.name}")
