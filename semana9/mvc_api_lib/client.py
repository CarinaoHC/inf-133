import requests

# URL base de la API
BASE_URL = "http://localhost:5000/api"

# Definir los encabezados de la solicitud
headers = {"Content-Type": "application/json"}

# Crear un nuevo book
url = f"{BASE_URL}/books"
nuevo_book = {"title": "Oceano", "author": "Oscar", "edition": 3, "availability": True}
response = requests.post(url, json=nuevo_book, headers=headers)
print("Creando un nuevo book:")
print(response.json())

# Crear el segundo book
book_2 = {"title": "La paciencia", "author": "Ana", "edition": 4, "availability": False}
response = requests.post(url, json=book_2, headers=headers)
print("\nCreando el segundo book:")
print(response.json())

# Crear el tercero book
book_3 = {"title": "Odisea", "author": "Homero", "edition": 1, "availability": True}
response = requests.post(url, json=book_3, headers=headers)
print("\nCreando el segundo book:")
print(response.json())

# Obtener la lista de todos los bookes
url = f"{BASE_URL}/books"
response = requests.get(url, headers=headers)
print("\nLista de books:")
print(response.json())

# Obtener un book específico por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/books/1"
response = requests.get(url, headers=headers)
print("\nDetalles del book con ID 1:")
print(response.json())

# Actualizar un book existente por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/books/1"
datos_actualizacion = {"title": "Lagrimas", "author": "Lidia", "edition": 3, "availability": True}
response = requests.put(url, json=datos_actualizacion, headers=headers)
print("\nActualizando el book con ID 1:")
print(response.json())

# Obtener la lista de todos los bookes
url = f"{BASE_URL}/books"
response = requests.get(url, headers=headers)
print("\nLista de books:")
print(response.json())

# Eliminar un book existente por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/books/1"
response = requests.delete(url, headers=headers)
print("\nEliminando el book con ID 1:")
if response.status_code == 204:
    print(f"book con ID 1 eliminado con éxito.")
else:
    print(f"Error: {response.status_code} - {response.text}")
    
# Obtener la lista de todos los bookes
url = f"{BASE_URL}/books"
response = requests.get(url, headers=headers)
print("\nLista de books:")
print(response.json())