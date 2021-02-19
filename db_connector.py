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


def adding_user(user_id: int, user_name: str) -> bool:
    try:
        cursor = get_cursor()
        cursor.execute(f"INSERT into users (user_id, user_name, creation_date) "
                        f"VALUES ('{user_id}', '{user_name}','{date.today()}')")
        cursor.close()
        return True
    except Exception:
        return False


def get_all_users() -> None:
    cursor = get_cursor()
    cursor.execute('SELECT * FROM users')
    cursor.close()
    for row in cursor:
        print(row)


def get_specific_user(user_id: int):
    cursor = get_cursor()
    cursor.execute(f'SELECT user_name FROM users WHERE user_id={user_id}')
    for row in cursor:
        return row


def update_user(user_id: int, user_name: str):
    cursor = get_cursor()
    cursor.execute(f'UPDATE users SET user_name="{user_name}" WHERE user_id={user_id}')
    cursor.close()


def delete_user(user_id: int):
    cursor = get_cursor()
    cursor.execute(f'DELETE FROM users WHERE user_id="{user_id}"')
    cursor.close()


