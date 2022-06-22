
# django
from django.urls import path,include

#django rest
from rest_framework.authtoken.views import obtain_auth_token

# models
from . import views

urlpatterns = [
    path(
        route='',
        view=views.drf_api_home,
        name='home'
    ),
    path(
        route='drf_post/',
        view=views.drf_api_post,
        name='drf_post'
    ),
    path(
        route='auth/',
        view=obtain_auth_token
    ),
    path('products/', include(('products.urls','products'), namespace='products')),
]
