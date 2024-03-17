#!/usr/bin/python3
""" display all values in the satate table with the matching name given """


from sys import argv
import MySQLdb

if (__name__ == '__main__'):

    check = False
    check_injection = (';', 'TRUNCATE ', 'SELECT ', 'WHERE ', 'FROM ',
                       'DELETE ', 'DROP ')
    for i in check_injection:
        if (i in argv[4]):
            check = True
            break
    if (not check):
        db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3])
        dbcursor = db.cursor()
        dbcursor.execute("SELECT * FROM states WHERE name LIKE '{}' COLLATE"
                         " utf8mb4_0900_as_cs ORDER BY id ASC".format(argv[4]))
        res = dbcursor.fetchall()
        for row in res:
            print(row)
