#!/usr/bin/python3
"""
"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    cur = conn.cursor()

    cur.execute("""SELECT c.id, c.name,
                s.name FROM cities c JOIN states s ON s.id
                = c.state_id""".format(sys.argv[4]))

    query_rows = cur.fetchall()

    p = []
    for row in query_rows:
        if row[2] == sys.argv[4]:
            p.append(row[1])

    boi = ', '.join(p)
    print(boi)

    cur.close()

    conn.close()
