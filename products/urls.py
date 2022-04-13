from django.urls import path

from .views import productsList, productsDetail


urlpatterns = [
    path('', productsList, name='products'),
    path('<int:product_id>/', productsDetail, name='products-detail'),
]
