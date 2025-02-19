import requests

#Own API GET request
api_url = "https://dog.ceo/api/breeds/image/random"
response = requests.get(api_url)
data = response.json()
print(f"Dog Image URL: {data['message']}")
