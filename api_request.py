import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response)
print(response.status_code)

if response.status_code == 200:
    print("Request Sucessful")
else:
    print("Request Unsuccessful")
    print(response.status_code)

data = response.json()
print(data["title"])