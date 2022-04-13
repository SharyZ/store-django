from django.urls import path

from .views import cartItemsList, cartItemDelete, cartItemUpdate


urlpatterns = [
    path('', cartItemsList, name='cart-items'),
    path('item/delete/<int:cart_item_id>/', cartItemsList, name='cart-item-delete'),
    path('item/update/<int:cart_item_id>/', cartItemUpdate, name='cart-item-update'),
]
