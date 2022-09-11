#!/usr/bin/python3
"""takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument
and is safe from SQL injections
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.arg[1], passwd=sys.argv[2], db=sys.argv[3],
                         host='localhost', port=3306)
    cur = db.cursor()
    cmd = """SELECT id, name
         FROM states
         WHERE name=%s
         ORDER BY id ASC"""
    cur.execute(cmd, (sys.argv[4],))
    nStates = cur.fetchall()

    for state in nStates:
        print(state)

    cur.close()
    db.close()
