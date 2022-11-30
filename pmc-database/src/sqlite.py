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


insert("Wine Glass", 10, 5.99)
insert("Coke Glass", 6, 7.99)
insert("Water Bottle", 12, 9.99)


def view():
    def fn(cursor):
        cursor.execute("SELECT * from store")
        return cursor.fetchall()

    return with_db(fn)


def remove(item):
    return with_db(lambda cursor: cursor.execute("DELETE FROM store WHERE item=?", (item,)))


def update(item, quantity, price):
    return with_db(
        lambda cursor: cursor.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item)))

print(view())

print(remove("Water Bottle"))

print(view())

update("Coke Glass", 10, 6.99)

print(view())

remove("Coke Glass")
remove("Wine Glass")

print(view())
