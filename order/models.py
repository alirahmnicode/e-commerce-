from django.db import models
from product.models import Product
from django.contrib.auth.models import User

from users.models import Profile

# Create your models here.
class Order(models.Model):
    user_info = models.ForeignKey(Profile , on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    payment = models.BooleanField(default=False)
    price_paid = models.IntegerField(default=0)
    trackingcode = models.BigIntegerField()
    confirm = models.BooleanField(default=False)
    post = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.price_paid}'