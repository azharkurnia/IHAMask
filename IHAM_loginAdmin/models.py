from django.db import models

# Create your models here.
class PromoCode(models.Model):
    promoName = models.CharField(max_length=10, blank=False)
    promoAmount = models.IntegerField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)