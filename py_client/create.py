import requests



"""GET whit Django Rest Framework"""
print('-'*20 + 'POST Create API View' + '-'*20)
endpoint = "http://localhost:8000/api/products/"

data = {
    'title': 'This field is done',
    'price': 32.00
}

get_response = requests.post(endpoint, json=data)
# print(get_response.text)  # print the raw response
print(f'response:{get_response.json()}')

