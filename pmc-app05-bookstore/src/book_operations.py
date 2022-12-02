import sqlite3


def with_db(fn):
    conn = sqlite3.connect("book_store.sqlite")
    result = fn(conn.cursor())
    conn.commit()
    conn.close()
    return result


def init_database():
    return with_db(lambda cur: cur.execute(
        'CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, year INTEGER, isbn INTEGER)'))


def create_book(title, author, year, isbn):
    book_attributes = (title, author, year, isbn)
    if any(val is None for val in book_attributes):
        raise Exception("All book attributes must be set!")

    return with_db(lambda cur: cur.execute('INSERT INTO books VALUES (?, ?, ?, ?)', book_attributes))


def update_book(title, author, year, isbn):
    book_attributes = (title, author, year, isbn)
    if any(val is None for val in book_attributes):
        raise Exception("All book attributes must be set!")

    return with_db(lambda cur: cur.execute("UPDATE books SET title=?, author=?, year=? WHERE isbn=?", book_attributes))


# def get_by_title(title):
#     return with_db(lambda cur: cur.execute("SELECT * FROM books WHERE title=?", (title,)))


init_database()
update_book("Bonsai Bug Battle Royale", "Peter Pan Deluxe", 2002, 123456789)
