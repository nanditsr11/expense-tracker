import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS expenses (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    date TEXT,
                                    category TEXT,
                                    amount REAL,
                                    description TEXT
                                )''')

    def add_expense(self, expense):
        with self.conn:
            self.conn.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
                              (expense['date'], expense['category'], expense['amount'], expense['description']))

    def get_expenses(self):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM expenses")
            return cursor.fetchall()
