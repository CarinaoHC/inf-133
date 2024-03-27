import requests
import json

url = "http://localhost:8000/chocolates"
headers = {"Content-Type": "application/json"}

# POST /chocolates
new_chocolate_data = {
    "chocolate_type": "tableta",
    "peso": 50,
    "sabor": "menta"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_chocolate_data = {
    "chocolate_type": "bonbon",
    "peso": 78,
    "sabor": "coco",
    "relleno": "crema de coco"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_chocolate_data = {
    "chocolate_type": "trufa",
    "peso": 10,
    "sabor": "frutilla",
    "relleno": "crema de cereza"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())


# GET /chocolates
response = requests.get(url=url)
print(response.json())

# PUT /chocolates/{chocolate_id}
chocolate_id_to_update = 1
updated_chocolate_data = {
    "sabor": "mora"
}
response = requests.put(f"{url}/{chocolate_id_to_update}", json=updated_chocolate_data)
print("Chocolate actualizado:", response.json())

# GET /chocolates
response = requests.get(url=url)
print(response.json())

# DELETE /chocolates/{chocolate_id}
chocolate_id_to_delete = 1
response = requests.delete(f"{url}/{chocolate_id_to_delete}")
print("Chocolate eliminado:", response.json())

# GET /chocolates
response = requests.get(url=url)
print(response.json())