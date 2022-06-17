import requests


"""GET whit Django Rest Framework"""
print('-'*20 + 'PUT Retrieve API View' + '-'*20)

product_id = input('what is the product id  you want to use?\n')
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} not a valid id')

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

get_response = requests.delete(endpoint)  # HTTP Request
print(get_response.status_code, get_response.status_code == 204)

