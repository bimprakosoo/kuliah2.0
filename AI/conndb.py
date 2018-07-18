import pymysql
import sys

class database:
    host = "localhost"
    user = "root"
    pasw = ""
    db   = "phishing_websites"

    try:
        conn = pymysql.connect(host = host, user = user, password = pasw, db = db, use_unicode=True, charset='utf8')
        print("TERKONEKSI DENGAN DATABASE")
        print("#####################################################")
    except Exception as e:
        sys.exit("KONEKSI DENGAN DATABASE GAGAL !!!!!", e)

    dbcursor = conn.cursor()
