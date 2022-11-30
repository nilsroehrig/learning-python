import sqlite3


def with_db(fn):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    result = fn(cursor)
    connection.commit()
    connection.close()
    return result


def create_store_table():
    return with_db(
        lambda cursor: cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)"))


def insert(item, quantity, price):
    return with_db(lambda cursor: cursor.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price)))


create_store_table()


# insert("Coke Glass", 6, 7.99)
# insert("Water Bottle", 12, 9.99)


def view():
    def fn(cursor):
        cursor.execute("SELECT * from store")
        return cursor.fetchall()

    return with_db(fn)


print(view())
