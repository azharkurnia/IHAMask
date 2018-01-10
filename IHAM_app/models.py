from django.db import models

# Create your models here.
class OrderList(models.Model):
    customerName = models.CharField(max_length=140, blank=False)
    customerEmail = models.EmailField(max_length=140, blank=False)
    customerPhone = models.IntegerField(blank=False)
    productQuantityA = models.IntegerField()
    productQuantityB = models.IntegerField()
    customerAddress = models.CharField(max_length=140, blank=False)
    totalPrice = models.IntegerField(blank=False)
    promoCode = models.CharField(max_length=140, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

class promoCode(models.Model):
	promoName = models.CharField(max_length=10, blank=False)
	promoAmount = models.FloatField(blank=False)
