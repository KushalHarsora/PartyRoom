import requests

# endpoint = "http://localhost:8000/anything"
endpoint = "https://httpbin.org/anything/"

response = requests.get(endpoint, json={
    "message": "hello",
})
print(response.json())