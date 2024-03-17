#!/usr/bin/python3
""" this script will list all satates from the database hbtn_0e_0_usa """


import sys
import MySQLdb

if (__name__ == '__main__'):
    uname = sys.argv[1]
    pswd = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=uname,
                         passwd=pswd, db=dbname)
    dbcursor = db.cursor()
    dbcursor.execute("SELECT * FROM states ORDER BY id ASC")
    res = dbcursor.fetchall()
    for row in res:
        print(row)
