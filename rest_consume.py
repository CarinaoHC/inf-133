import requests
card_numer = "BT1-010"
url = f"https://digimoncard.io/api-public/search.php?card={card_numer}"

response = requests.request(
    method="GET",
    url=url,
    headers={"Content-Type": "application/json"},
    data={}
)
print(response.text)