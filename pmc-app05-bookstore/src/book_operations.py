import sqlite3


def with_db(fn):
    conn = sqlite3.connect("book_store.sqlite")
    result = fn(conn.cursor())
    conn.commit()
    conn.close()
    return result


def init_database():
    return with_db(lambda cur: cur.execute(
        'CREATE TABLE IF NOT EXISTS books (title TEXT NOT NULL, author TEXT NOT NULL, year INTEGER NOT NULL, isbn INTEGER PRIMARY KEY)'))


def create_book(title, author, year, isbn):
    return with_db(lambda cur: cur.execute('INSERT INTO books VALUES (?, ?, ?, ?)', (title, author, year, isbn)))


def update_book(title, author, year, isbn):
    return with_db(
        lambda cur: cur.execute("UPDATE books SET title=?, author=?, year=? WHERE isbn=?", (title, author, year, isbn)))


def remove_book(isbn):
    return with_db(lambda cur: cur.execute("DELETE FROM books WHERE isbn=?", (isbn,)))


# def get_by_title(title):
#     return with_db(lambda cur: cur.execute("SELECT * FROM books WHERE title=?", (title,)))

init_database()
remove_book(123456789)
