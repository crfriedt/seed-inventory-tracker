import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS seeds (id INTEGER PRIMARY KEY, strain text, types text, date text, quantity text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM seeds")
        rows = self.cur.fetchall()
        return rows

    def insert(self, strain, types, date, quantity):
        self.cur.execute("INSERT INTO seeds VALUES (NULL, ?, ?, ?, ?)", (strain, types, date, quantity))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM seeds WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, strain, types, date, quantity):
        self.cur.execute("UPDATE seeds SET strain = ?, types = ?, date = ?, quantity = ? WHERE id = ?", (strain, types, date, quantity,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()