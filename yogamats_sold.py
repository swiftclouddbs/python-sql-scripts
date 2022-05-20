import sys
import cx_Oracle
import os




if os.path.exists("yogamatssold"):
	os.remove("yogamatssold")
	print("File removed.")
else:
	print("No yogamatssold file here")


cx_Oracle.init_oracle_client(lib_dir="/usr/lib/oracle/21/client64/lib")

con = cx_Oracle.connect(user="curious", password="access*SOL", dsn="adw-xyz")


sys.stdout = open('yogamatssold', 'w')

cur = con.cursor()


sql0 = "select count(*) from jun2021vaersdata where state = 'MD' and age_yrs BETWEEN 30 and 50"

cur.execute(sql0)
count = cur.fetchone()

print(count, "Total mats sold in MD")

sql1 = "select count(*) from jun2021vaersdata where state = 'MD' and age_yrs BETWEEN 30 and 50 and sex = 'F'"

cur.execute(sql1)
count1 = cur.fetchone()

print(count1, "Total mats sold to women between ages 30 and 50")

sql2 = "select count(*) from jun2021vaersdata where state = 'MD' and age_yrs BETWEEN 30 and 50 and sex = 'M'"

cur.execute(sql2)
count2 = cur.fetchone()
print(count2, "Total mats sold to men between ages 30 and 50")


sys.stdout.close
