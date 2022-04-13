from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class CartItem(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ForeignKey(CartItem, on_delete=models.CASCADE)
