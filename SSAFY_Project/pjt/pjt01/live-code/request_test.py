import requests
from pprint import pprint

url = "https://fakestoreapi.com/carts"

# API 요청 보내기
response = requests.get(url).json()
print(type(response))
print(type(response[0]))
# pprint(response)