#!/usr/bin/python3
""" lists all cities from the database """


import MySQLdb
from sys import argv

if (__name__ == '__main__'):
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    dbcursor = db.cursor()
    dbcursor.execute("SELECT cities.id, cities.name, states.name FROM cities"
                     " INNER JOIN states ON cities.state_id = states.id")
    res = dbcursor.fetchall()
    for row in res:
        print(row)
