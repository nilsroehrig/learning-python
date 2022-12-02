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


def get_all_books():
    return with_db(lambda cur: cur.execute("SELECT * from books").fetchall())


def find_books(title, author, year, isbn):
    if isbn is not None:
        return with_db(lambda cur: cur.execute("SELECT * from books WHERE isbn=?", (isbn,)).fetchall())

    if all(v is None for v in (title, author, year)):
        return []

    query_values = ()
    query_conditions = ()

    if title is not None:
        query_values += (title,)
        query_conditions += ("title=?",)

    if author is not None:
        query_values += (author,)
        query_conditions += ("author=?",)

    if year is not None:
        query_values += (year,)
        query_conditions += ("year=?",)

    condition_string = " AND ".join(query_conditions)
    query = "SELECT * from books WHERE %s" % condition_string

    return with_db(lambda cur: cur.execute(query, query_values).fetchall())


init_database()

