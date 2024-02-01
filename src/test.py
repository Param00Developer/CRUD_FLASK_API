import requests

BASE = "http://127.0.0.1:5000/"

data={"name":"Param","age":21,"salary":20000}
response = requests.get(BASE + "user/2")
print(response.json())