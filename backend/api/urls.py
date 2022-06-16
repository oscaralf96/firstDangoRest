from django.urls import path,include
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
    path('products/', include(('products.urls','products'), namespace='products')),
]
