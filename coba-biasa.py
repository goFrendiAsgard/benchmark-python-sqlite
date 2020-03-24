import sqlite3 as lite
import time
from common import create_table_sql, insert_sql, data, drop_table_sql

con = None

try:

    start = time.time()

    con = lite.connect('test-biasa.db')
    cur = con.cursor()

    cur.execute(drop_table_sql)
    cur.execute(create_table_sql)

    for row in data:
        cur.execute(insert_sql.format(*row))
    con.commit()

    end = time.time()
    print("biasa elapsed time:\t", end-start)

except lite.Error as e:
    print("Error {}:".format(e.args[0]))
finally:
    if con:
        con.close()
