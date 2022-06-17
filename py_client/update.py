import requests


"""GET whit Django Rest Framework"""
print('-'*20 + 'PUT Retrieve API View' + '-'*20)
endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    'title': 'hello my old friend',
    'price': 129.99
}

get_response = requests.put(endpoint, json=data)  # HTTP Request
# print(get_response.text)  # print the raw response
print(f'response:{get_response.json()}')

