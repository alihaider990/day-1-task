import requests
import time

def fetch_and_display_users():
    print("Loading..")  
    time.sleep(1)        

    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response.raise_for_status()
        users = response.json()
        print("User List:\n")
        print(users)  

        
        for user in users:
            name = user.get("name")
            email = user.get("email")
            city = user.get("address", {}).get("city")
            print(f"{name} - {email} - {city}")
    except requests.RequestException:
        print("Something went wrong!")  

if __name__ == "__main__":
    fetch_and_display_users()