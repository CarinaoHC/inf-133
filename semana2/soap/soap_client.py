from zeep import Client
client = Client(
    "http://localhost:8000/"
)
result = client.service.Saludar(nombre="karina")
print(result)
result1 = client.service.CadenaPalindromo(cadena="hola")
print(result1)