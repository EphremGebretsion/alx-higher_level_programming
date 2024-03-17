#!/usr/bin/python3
""" lists all states with a name starting with N """


from sys import argv
import MySQLdb

if (__name__ == '__main__'):
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    dbcursor = db.cursor()
    dbcursor.execute("SELECT * FROM states WHERE name LIKE 'N%'"
                     "COLLATE utf8mb4_0900_as_cs ORDER BY id ASC")
    res = dbcursor.fetchall()
    for row in res:
        print(row)
