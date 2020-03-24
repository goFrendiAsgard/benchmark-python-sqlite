import sqlite3 as lite
import time
from common import create_table_sql, insert_bulk_sql, data, drop_table_sql

con = None

try:

    start = time.time()

    con = lite.connect('test-bulk.db')
    cur = con.cursor()

    cur.execute(drop_table_sql)
    cur.execute(create_table_sql)

    cur.executemany(insert_bulk_sql, data)
    con.commit()

    end = time.time()
    print("bulk elapsed time:\t", end-start)

except lite.Error as e:
    print("Error {}:".format(e.args[0]))
finally:
    if con:
        con.close()
