from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100,unique=True)
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    is_active = models.BooleanField()

