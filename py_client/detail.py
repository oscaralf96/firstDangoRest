import requests



"""GET whit Django Rest Framework"""
print('-'*20 + 'GET Retrieve API View' + '-'*20)
endpoint = "http://localhost:8000/api/products/2/"

get_response = requests.get(endpoint, json={"title": "ABC123", "content": "Hello world"})  # HTTP Request
# print(get_response.text)  # print the raw response
print(f'response:{get_response.json()}')

