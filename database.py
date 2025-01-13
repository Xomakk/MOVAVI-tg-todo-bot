import sqlite3


def create_con():
    return sqlite3.connect("data.db")


def create_tables():
    con = create_con()

    # Задача: id, title, status, user_id
    SQL = """
        CREATE TABLE IF NOT EXISTS task (
            id INTEGER PRIMARY KEY,
            title TEXT,
            user_id INTEGER,
            status BOOL
        )
    """
    con.execute(SQL)
