import requests
# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Definir la consulta GraphQL simple
query_lista = """
{
        estudiantes{
            id
            nombre
            apellido
            carrera
        }
    }
"""
# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query_lista})
print(response.text)

# Definir la consulta GraphQL para crear nuevo estudiante 1
query_crear = """
mutation {
        crearEstudiante(nombre: "Angel", apellido: "Gomez", carrera: "Biologia") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_crear})
print(response_mutation.text)

# Definir la consulta GraphQL para crear nuevo estudiante 2
query_crear2 = """
mutation {
        crearEstudiante(nombre: "Maria", apellido: "Perez", carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation2 = requests.post(url, json={'query': query_crear2})
print(response_mutation2.text)

# Definir la consulta GraphQL para crear nuevo estudiante 3
query_crear3 = """
mutation {
        crearEstudiante(nombre: "Oscar", apellido: "Iglesias", carrera: "Matematicas") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation3 = requests.post(url, json={'query': query_crear3})
print(response_mutation3.text)

# Lista de todos los estudiantes
response = requests.post(url, json={'query': query_lista})
print(response.text)

# Definir la consulta GraphQL para eliminar un estudiante
query_eliminar = """
mutation {
        deleteEstudiante(id: 3) {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_eliminar})
print(response_mutation.text)

# Lista de todos los estudiantes
response = requests.post(url, json={'query': query_lista})
print(response.text)


query_actualizar = """
mutation {
        actualizarEstudiante(nombre: "Jose", apellido: "Lopez") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation_ac = requests.post(url, json={'query': query_actualizar})
print(response_mutation_ac.text)

# Lista de todos los estudiantes
response = requests.post(url, json={'query': query_lista})
print(response.text)