import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "My custom title is this",
    "body": "This is body of my post.",
    "userId": 1
}
headers = {
    "Content-type": "application/json; charset=UTF-8"
}

try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    print("Response from POST request:")
    print(response.json())
except requests.RequestException as l:
    print("Error creating post:", l)