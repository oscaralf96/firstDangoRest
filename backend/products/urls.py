from django.urls import path
from . import views

urlpatterns = [
    path(
        route='create/',
        view=views.ProductCreateAPIView.as_view(),
        name='create'
    ),
    path(
        route='list_create/',
        view=views.ProductListCreateAPIView.as_view(),
        name='create_list'
    ),
    path(
        route='<int:pk>/',
        view=views.ProductDetailAPIView.as_view(),
        name='products'
    ),
]

