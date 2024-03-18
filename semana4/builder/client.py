import requests

url = "http://localhost:8000/pizza"
headers = {'Content-type': 'application/json'}

mi_pizza = {
    "tamaño": "Grande",
    "masa": "Delgada",
    "toppings": ["Jamon", "Queso"]
}
response = requests.post(url, json=mi_pizza, headers=headers)
print(response.json())

mi_pizza2 = {
    "tamaño": "Pequeño",
    "masa": "Gruesa",
    "toppings": ["Piña", "Carne"]
}
response = requests.post(url, json=mi_pizza2, headers=headers)
print(response.json())