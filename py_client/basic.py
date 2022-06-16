import requests
import urllib.request
from bs4 import BeautifulSoup



"""GET whit Django Rest Framework"""
print('-'*20 + 'GET' + '-'*20)
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"


#get_response = requests.get(endpoint, data={"query": "Hello world!"})  # HTTP Request
#get_response = requests.get(endpoint, params = {'abc': '123'}, json={"query": "Hello world!"})  # HTTP Request
get_response = requests.get(endpoint, json={"query": "Hello world!"})  # HTTP Request
# get_response = requests.get(endpoint)

print(get_response.text)  # print the raw response
#print(get_response.json()['message'])
print(f'response:{get_response}')

"""POST whit Django Rest Framework"""
print('-'*20 + 'POST' + '-'*20)

endpoint = "http://localhost:8000/api/drf_post/"
get_response = requests.post(endpoint, json={"title": "ABC123", "content": "Hello world"})  # HTTP Request
print(get_response.text)  # print the raw response
print(f'response:{get_response}')



"""Beautiful Soup"""
#get_response = urllib.request.urlopen(endpoint)
#html = get_response.read()
#soup = BeautifulSoup(html).encode("utf-8")

#print(f'response:{get_response}')
#print(soup)
#print(html)