import MySQLdb
from flask import request

def connection():
    conn = MySQLdb.connect(host="127.0.01",
                           user="root",
                           passwd="",
                           db = "arclab")

    c = conn.cursor()

    return c, conn

    try:
            c, conn = connection()

            if request.method == "GET":

                x = c.execute("SELECT * FROM post")
                Post = c.fetchall()

                for row in Post:
                    print row
                   # urls = {"URLS":[['id', row[0]], ['title', row[1]], ['body', row[2]], ['date', row[3]], ['author', row[4]], ['comments',row[5]], ['urls',row[6]]]}

            c.close()
            conn.close()

            #return urls[URLS]

           # print (urls[URLS])

    except Exception as exc:
                return (str(exc))
