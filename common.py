create_table_sql = "CREATE TABLE IF NOT EXISTS abcd (a integer, b integer, c integer, d integer, e integer, f integer, g integer, h integer, i integer, j integer, k integer, l integer, m integer, n integer, o integer, p integer, q integer, r integer, s integer, t integer, u integer);"

insert_sql = "INSERT INTO abcd(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u) VALUES({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})"
insert_bulk_sql = "INSERT INTO abcd(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"


row = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1]
data = [row for x in range (1000000)]

drop_table_sql = "DROP TABLE IF EXISTS abcd"
