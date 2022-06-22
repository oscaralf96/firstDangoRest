# django rest framework
from rest_framework.authentication import TokenAuthentication as BaseTokenAuth


class TokenAuthentication(BaseTokenAuth):
    keyword = 'Bearer'
