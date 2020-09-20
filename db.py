import sqlite3

__connection = None


def log_error(f):
    def inner(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except Exception as e:
            print(f"ощибка: {e}")
            raise e

    return inner


def get_connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect("database.db", check_same_thread=False)
    return __connection


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, title TEXT, description TEXT)")
    connection.commit()

def get_all_events():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events")
    return cursor.fetchall()
