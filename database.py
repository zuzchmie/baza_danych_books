import sqlite3
from models import Book


class Database:
    def __init__(self, db_name="books.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER
            )
        """)
        self.connection.commit()

    def add_book(self, book: Book):
        self.cursor.execute(
            "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
            (book.title, book.author, book.year)
        )
        self.connection.commit()

    def delete_book(self, title):
        self.cursor.execute(
            "DELETE FROM books WHERE title = ?",
            (title,)
        )

        if self.cursor.rowcount == 0:
            return False  
        else:
            self.connection.commit()
            return True
        

    def search_books(self, keyword):
        self.cursor.execute(
            "SELECT title, author, year FROM books WHERE title LIKE ? OR author LIKE ?",
            (f"%{keyword}%", f"%{keyword}%")
        )
        return self.cursor.fetchall()

    def list_books(self):
        self.cursor.execute("SELECT title, author, year FROM books")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
