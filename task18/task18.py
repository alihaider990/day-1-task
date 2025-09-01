import requests


try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    response.raise_for_status()  
    posts = response.json()
    print("First 5 post titles:")
    for post in posts[:5]:
        print(post["title"])
except requests.RequestException as e:
    print("Error fetching all posts:", e)


try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    response.raise_for_status()
    post = response.json()
    print("\nSingle post (/posts/1):")
    print(post)
except requests.RequestException as e:
    print("Error fetching single post:", e)


try:
    response = requests.get("https://jsonplaceholder.typicode.com/wrongurl")
    response.raise_for_status()
    data = response.json()
    print("\nWrong URL response:")
    print(data)
except requests.RequestException as e:
    print("\nError with wrong URL:", e)