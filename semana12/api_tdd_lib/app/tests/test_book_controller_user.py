def test_get_books_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" debería poder obtener la lista de libros
    response = test_client.get("/api/books", headers=user_auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_book(test_client, admin_auth_headers):
    data = {"title": "La oscuridad", "author": "Oscar", "edition": 2, "availability": True}
    response = test_client.post("/api/books", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["title"] == "La oscuridad"
    assert response.json["author"] == "Oscar"
    assert response.json["edition"] == 2
    assert response.json["availability"] == True


def test_get_book_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" debería poder obtener un book específico
    # Este test asume que existe al menos un book en la base de datos
    response = test_client.get("/api/books/1", headers=user_auth_headers)
    assert response.status_code == 200
    assert "title" in response.json


def test_create_book_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder crear un book
    data = {"title": "Poesia", "author": "Paola", "edition": 3, "availability": True}
    response = test_client.post("/api/books", json=data, headers=user_auth_headers)
    assert response.status_code == 403


def test_update_book_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder actualizar un book
    data = {"title": "Odisea", "author": "Anonimo", "edition": 1, "availability": True}
    response = test_client.put("/api/books/1", json=data, headers=user_auth_headers)
    assert response.status_code == 403


def test_delete_book_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder eliminar un book
    response = test_client.delete("/api/books/1", headers=user_auth_headers)
    assert response.status_code == 403