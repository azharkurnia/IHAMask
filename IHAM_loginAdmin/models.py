from django.db import models

# Create your models here.
class PromoCode(models.Model):
    promoCode = models.CharField(max_length=10, blank=False)
    promoAmount = models.IntegerField(blank=False)
    