import sqlite3 as lite
import time
from common import create_table_sql, insert_sql, data, drop_table_sql
from concurrent.futures import ProcessPoolExecutor

con = None

try:

    start = time.time()

    con = lite.connect('test-process.db')
    cur = con.cursor()

    cur.execute(drop_table_sql)
    cur.execute(create_table_sql)

    params = [insert_sql.format(*row) for row in data]

    with ProcessPoolExecutor() as executor:
        executor.map(cur.execute, params)
    con.commit()

    end = time.time()
    print("process elapsed time:\t", end-start)

except lite.Error as e:
    print("Error {}:".format(e.args[0]))
finally:
    if con:
        con.close()
