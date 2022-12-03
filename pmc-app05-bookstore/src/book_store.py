from tkinter import *

from book_operations import get_all_books, create_book


def all_set():
    return all(len(var.get()) > 0 for var in (var_title, var_author, var_year, var_isbn))


def isbn_known():
    return var_isbn.get() in [isbn for _, _, _, isbn in var_books.get()]


def load_book():
    if len(lst_books.curselection()) == 0:
        return

    title, author, year, isbn = lst_books.get(lst_books.curselection())

    var_title.set(title)
    var_author.set(author)
    var_year.set(year)
    var_isbn.set(isbn)


def add_book():
    if not all_set():
        return

    if isbn_known():
        return

    create_book(var_title.get(), var_author.get(), var_year.get(), var_isbn.get())

    var_books.set(get_all_books())


book_store = Tk()
book_store.title("Book Store")

lbl_title = Label(book_store, text="Title")
var_title = StringVar()
ent_title = Entry(book_store, textvariable=var_title)

lbl_author = Label(book_store, text="Author")
var_author = StringVar()
ent_author = Entry(book_store, textvariable=var_author)

lbl_year = Label(book_store, text="Year")
var_year = StringVar()
ent_year = Entry(book_store, textvariable=var_year)

lbl_isbn = Label(book_store, text="ISBN")
var_isbn = StringVar()
ent_isbn = Entry(book_store, textvariable=var_isbn)

btn_add = Button(book_store, text="Add Book", command=add_book)
btn_update = Button(book_store, text="Update Book")
btn_search = Button(book_store, text="Search Book")
btn_quit = Button(book_store, text="Quit", command=book_store.quit)

var_books = Variable(value=get_all_books())
lst_books = Listbox(book_store, height=10, listvariable=var_books)

btn_load = Button(book_store, text="Load Selected", command=load_book)
btn_delete = Button(book_store, text="Delete selected")

lbl_title.grid(row=0, column=0, padx=5, pady=5, sticky="w")
ent_title.grid(row=0, column=1, padx=5, pady=5, sticky=W + E)

lbl_author.grid(row=1, column=0, padx=5, pady=5, sticky="w")
ent_author.grid(row=1, column=1, padx=5, pady=5, sticky=W + E)

lbl_year.grid(row=2, column=0, padx=5, pady=5, sticky="w")
ent_year.grid(row=2, column=1, padx=5, pady=5, sticky=W + E)

lbl_isbn.grid(row=3, column=0, padx=5, pady=5, sticky="w")
ent_isbn.grid(row=3, column=1, padx=5, pady=5, sticky=W + E)

btn_add.grid(row=0, column=2, padx=5, pady=5, sticky=W + E)
btn_update.grid(row=1, column=2, padx=5, pady=5, sticky=W + E)
btn_search.grid(row=2, column=2, padx=5, pady=5, sticky=W + E)
btn_quit.grid(row=3, column=2, padx=5, pady=5, sticky=W + E)

lst_books.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky=W + E)

btn_load.grid(row=5, column=1, padx=5, pady=5, sticky=W + E)
btn_delete.grid(row=5, column=2, padx=5, pady=5, sticky=W + E)

book_store.mainloop()
