from django.urls import path
from . import views

urlpatterns = [
    path(
        route='',
        view=views.ProductCreateAPIView.as_view(),
        name='create'
    ),
    path(
        route='<int:pk>/',
        view=views.ProductDetailAPIView.as_view(),
        name='products'
    )
]

