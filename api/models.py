from django.db import models

# Create your models here
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)    
    

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=250, default="Unkown")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders', default=1)
    amount = models.IntegerField(default=1)
    current_event  = models.CharField(max_length=100, default="Pending")
    

    