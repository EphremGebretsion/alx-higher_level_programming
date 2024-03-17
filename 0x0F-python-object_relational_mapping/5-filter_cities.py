#!/usr/bin/python3
""" lists all the cities of the given state """


from MySQLdb import connect
from sys import argv

if (__name__ == '__main__'):
    inj = (';', 'TRUNCATE ', 'WHERE ', 'SELECT ', 'FROM ', 'DROP ', 'DELETE ')
    check = False
    for i in inj:
        if (i in argv[4].upper()):
            check = True
            break
    if (not check):
        db = connect(host='localhost', port=3306, user=argv[1],
                     passwd=argv[2], db=argv[3])
        dbcursor = db.cursor()
        dbcursor.execute("SELECT cities.name FROM cities "
                         "INNER JOIN states ON states.id = cities.state_id "
                         "WHERE states.name = '{}' "
                         "ORDER BY cities.id ASC".format(argv[4]))
        res = dbcursor.fetchall()
        after = ''
        for row in res:
            print(after + row[0], end='')
            after = ', '
        print('')
