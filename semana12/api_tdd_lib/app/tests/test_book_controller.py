def test_get_books(test_client, auth_headers):
    response = test_client.get("/api/books", headers=auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_book(test_client, auth_headers):
    data = {"title": "La oscuridad", "author": "Oscar", "edition": 2, "availability": True}
    response = test_client.post("/api/books", json=data, headers=auth_headers)
    assert response.status_code == 201
    assert response.json["title"] == "La oscuridad"


def test_get_book(test_client, auth_headers):
    # Primero crea un book
    data = {"title": "Poesia", "author": "Paola", "edition": 3, "availability": True}
    response = test_client.post("/api/books", json=data, headers=auth_headers)
    assert response.status_code == 201
    book_id = response.json["id"]

    # Ahora obtén el book
    response = test_client.get(f"/api/books/{book_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json["title"] == "Poesia"


def test_update_book(test_client, auth_headers):
    # Primero crea un book
    data = {"title": "Odisea", "author": "Anonimo", "edition": 1, "availability": True}
    response = test_client.post("/api/books", json=data, headers=auth_headers)
    assert response.status_code == 201
    book_id = response.json["id"]

    # Ahora actualiza el book
    update_data = {"title": "Odisea", "author": "Homero", "edition": 2, "availability": True}
    response = test_client.put(
        f"/api/books/{book_id}", json=update_data, headers=auth_headers
    )
    assert response.status_code == 200
    assert response.json["author"] == "Homero"
    assert response.json["edition"] == 2
    assert response.json["availability"] == True


def test_delete_book(test_client, auth_headers):
    # Primero crea un book
    data = {"title": "Redireccion", "author": "anonimo", "edition": 3, "availability": False}
    response = test_client.post("/api/books", json=data, headers=auth_headers)
    assert response.status_code == 201
    book_id = response.json["id"]

    # Ahora elimina el book
    response = test_client.delete(f"/api/books/{book_id}", headers=auth_headers)
    assert response.status_code == 204

    # Verifica que el book ha sido eliminado
    response = test_client.get(f"/api/books/{book_id}", headers=auth_headers)
    assert response.status_code == 404