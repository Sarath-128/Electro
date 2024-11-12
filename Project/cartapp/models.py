
from django.db import models
from myapp.models import ProductDetails
from django.contrib.auth.models import User

class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE , null=True)
    items=models.ManyToManyField(ProductDetails)

class CartItems(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    book=models.ForeignKey(ProductDetails,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
