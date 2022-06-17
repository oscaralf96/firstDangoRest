from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.product_mixin_view, name='create'),
    path(route='<int:pk>/', view=views.product_mixin_view, name='detail'),
    path(route='list/', view=views.ProductListAPIView.as_view(), name='list'),
    path(route='<int:pk>/update/', view=views.product_update_view, name='update'),
    path(route='<int:pk>/delete/', view=views.product_delete_view, name='delete'),


]

"""path(
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
        route='alt_view/',
        view=views.product_alt_view,
        name='alt_view'
    ),
    path(
        route='<int:pk>/',
        view=views.product_alt_view,
        name='products'
    ),"""