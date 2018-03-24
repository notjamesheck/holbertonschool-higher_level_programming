#!/usr/bin/python3

import MySQLdb
import argv from sys

conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                       passwd=argv[2], db=argv[3])

cur = conn.cursor()

cur.execute("SELECT * FROM states ORDER BY id ASC")

query_rows = cur.fetchall()

for row in query_rows:
    print(row)

cur.close()

conn.close()
