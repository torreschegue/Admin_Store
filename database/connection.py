import sqlite3

class DatabaseConnection:
    def __init__(self, db_name="inventary.db"):
        self.db_name = db_name

    def get_connection(self ):
        return sqlite3.connect(self.db_name)


    def create_tables(self):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                stock INTEGER NOT NULL,
                active INTEGER NOT NULL
            )
        """)
        connection.commit()
        cursor.close()