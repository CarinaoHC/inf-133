def test_get_books(test_client, admin_auth_headers):
    response = test_client.get("/api/books", headers=admin_auth_headers)
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


def test_get_book(test_client, admin_auth_headers):
    # Primero crea un book
    data = {"title": "Poesia", "author": "Paola", "edition": 3, "availability": True}
    response = test_client.post("/api/books", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    book_id = response.json["id"]

    # Ahora obtén el book
    response = test_client.get(f"/api/books/{book_id}", headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json["title"] == "Poesia"
    assert response.json["author"] == "Paola"
    assert response.json["edition"] == 3
    assert response.json["availability"] == True


def test_get_nonexistent_book(test_client, admin_auth_headers):
    response = test_client.get("/api/books/999", headers=admin_auth_headers)
    print(response.json)
    assert response.status_code == 404
    assert response.json["error"] == "Book no encontrado"


def test_create_book_invalid_data(test_client, admin_auth_headers):
    data = {"title": "Cien años de soledad"}  # Falta autor, edicion y disponibilidad
    response = test_client.post("/api/books", json=data, headers=admin_auth_headers)
    assert response.status_code == 400
    assert response.json["error"] == "Faltan datos requeridos"


def test_update_book(test_client, admin_auth_headers):
    # Primero crea un book
    data = {"title": "Odisea", "author": "Anonimo", "edition": 1, "availability": True}
    response = test_client.post("/api/books", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    book_id = response.json["id"]

    # Ahora actualiza el book
    update_data = {"title": "Odisea", "author": "Homero", "edition": 2, "availability": True}
    response = test_client.put(
        f"/api/books/{book_id}", json=update_data, headers=admin_auth_headers
    )
    assert response.status_code == 200
    assert response.json["title"] == "Odisea"
    assert response.json["author"] == "Homero"
    assert response.json["edition"] == 2
    assert response.json["availability"] == True


def test_update_nonexistent_book(test_client, admin_auth_headers):
    update_data = {"title": "Libre", "author": "anonimo", "edition": 1, "availability": True}
    response = test_client.put(
        "/api/books/999", json=update_data, headers=admin_auth_headers
    )
    print(response.json)
    assert response.status_code == 404
    assert response.json["error"] == "Book no encontrado"


def test_delete_book(test_client, admin_auth_headers):
    # Primero crea un book
    data = {"title": "Redireccion", "author": "anonimo", "edition": 3, "availability": False}
    response = test_client.post("/api/books", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    book_id = response.json["id"]

    # Ahora elimina el book
    response = test_client.delete(f"/api/books/{book_id}", headers=admin_auth_headers)
    assert response.status_code == 204

    # Verifica que el book ha sido eliminado
    response = test_client.get(f"/api/books/{book_id}", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Book no encontrado"
    
    
def test_delete_nonexistent_book(test_client, admin_auth_headers):
    response = test_client.delete("/api/books/999", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Book no encontrado"