from django.db import models

# Create your models here.
class OrderList(models.Model):
    customerName = models.CharField(max_length=140, blank=False)
    customerEmail = models.EmailField(max_length=140, blank=False)
    customerPhone = models.IntegerField(max_length=14, blank=False)
    productQuantityA = models.IntegerField(max_length=5)
    productQuantityB = models.IntegerField(max_length=5)
    customerAddress = models.CharField(max_length=140, blank=False)
    totalPrice = models.IntegerField(max_length=10, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
