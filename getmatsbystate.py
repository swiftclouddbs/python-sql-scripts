import cx_Oracle
import sys
import os

if os.path.exists("statenums"):
	os.remove("statenums")
else:
	print("No results file here")



cx_Oracle.init_oracle_client(lib_dir="/usr/lib/oracle/21/client64/lib")

con = cx_Oracle.connect(user="boss", password="yogamats", dsn="adwyoga_low")

sys.stdout = open('statenums', 'w')

cur = con.cursor()

sql0 = "select count(distinct state) from jun2021yogadata"

cur.execute(sql0)
res = cur.fetchall()
total_records = (res[0][0])
#print(total_records, "Records Produced By Query")

cur.prefetchrows = total_records
cur.arraysize = total_records
#cur.execute(sql0)

#print()
#print()

#print(total_records)
#res = cur.fetchall()

sql1 = "select distinct state from jun2021yogadata order by state asc"

cur.execute(sql1)
res = cur.fetchall()


for x in res:

    sql2 = "select count(*) from jun2021yogadata where state = :id"

    cur.execute(sql2, id = x[0])

    record = cur.fetchall()
    print(record, x[0])





sys.stdout.close()

