from flask import render_template
from flask_login import current_user


# La función `list_books` recibe una lista de
# bookes y renderiza el template `books.html`
def list_books(books):
    return render_template(
        "books.html",
        books=books,
        title="Lista de books",
        current_user=current_user,
    )


# La función `create_book` renderiza el
# template `create_book.html` o devuelve un JSON
# según la solicitud
def create_book():
    return render_template(
        "create_book.html", title="Crear book", current_user=current_user
    )


# La función `update_book` recibe un book
# y renderiza el template `update_book.html`
def update_book(book):
    return render_template(
        "update_book.html",
        title="Editar book",
        book=book,
        current_user=current_user,
    )