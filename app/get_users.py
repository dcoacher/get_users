import requests

# Users List Dummy Data Origin: "https://dummyjson.com/users?limit=85"

download_users = requests.get("https://dummyjson.com/users?limit=85")   # Downloading Data

# print(download_users)
users = download_users.json().get("users",[])   # Printing Data
print(users[0]["firstName"])

for user in users:
    print(user["firstName"])