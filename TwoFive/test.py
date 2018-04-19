from  __future__ import print_function
from db_connect import connection

c, conn = connection()
# if request.method == "GET":


x = c.execute("SELECT * FROM post")
x = c.fetchall()
for row in x:

    print(row[1], row[2])

c.close()
conn.close()
