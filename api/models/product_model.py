from django.db import models

# Create your models here
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)    