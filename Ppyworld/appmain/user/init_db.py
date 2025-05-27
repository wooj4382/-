import sqlite3

def init_db():
    conn = sqlite3.connect('pyBook.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            passwd TEXT NOT NULL,
            authkey TEXT
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    init_db()