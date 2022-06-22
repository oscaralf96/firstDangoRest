import requests
from getpass import getpass

"""Get Django Rest Framework Auth Token"""
print('-'*20 + 'Get Django Rest Framework Auth Token' + '-'*20 + '\n')

auth_endpoint = "http://localhost:8000/api/auth/"
username = "cfe"
password = "123"  # getpass()

auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:

    """GET whit Django Rest Framework"""
    print('-'*20 + 'GET List Create API View' + '-'*20 + '\n')

    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/products/"

    data = {
        'title': 'This field is done',
        'price': 32.00
    }

    get_response = requests.get(url=endpoint, json=data, headers=headers)
    print(f'response:{get_response.json()}')

