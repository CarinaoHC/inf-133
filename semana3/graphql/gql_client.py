import requests

# Definir la consulta GraphQL
query = """
    {
        estudiantes{
            id
            nombre
            apellido
            carrera
        }
        
    }
"""
query2 = """
    {
        estudiantes{
            nombre
        }
        
    }
"""
query3 = """
    {
        estudiantes{
            nombre
            apellido
        }
        
    }
"""

# Definir la URL del servidor GraphQL
url = "http://localhost:8000/graphql"

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={"query": query})
print(response.text)
