import sqlite3

def create_table():
    """
    The create_table function creates a new table called Tasks in a Database called taskpal_db.db
    """
    my_conn = sqlite3.connect("taskpal_db.db")
    my_cur = my_conn.cursor()

    my_cur.execute("""CREATE TABLE IF NOT EXISTS Tasks (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100),
        description TEXT,
        estimatedTime INTEGER,
        priority INTEGER,
        status INTEGER,
        createdAt VARCHAR(50),
        dueDate VARCHAR(50)
    );
    """)

    my_conn.commit()
    my_conn.close()
