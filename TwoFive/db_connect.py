import MySQLdb

def connection():
    conn = MySQLdb.connect(host="127.0.01",
                           user="root",
                           passwd="",
                           db = "arclab")
    
    c = conn.cursor()

    return c, conn
