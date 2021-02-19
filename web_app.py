import pymysql
from datetime import date

HOST = "sql2.freemysqlhosting.net"
PORT = 3306
USER = "sql2392763"
PASSWORD = "vA9*hW7%"
DB = "sql2392763"


def get_cursor():
    conn = pymysql.connect(host=HOST, port=PORT,
                           user=USER, passwd=PASSWORD, db=DB)
    conn.autocommit(True)
    return conn.cursor()


def get_user_name_from_db(user_id: int):
    cursor = get_cursor()
    cursor.execute(f'SELECT user_name FROM users WHERE user_id={user_id}')
    for row in cursor:
        return str(row)





