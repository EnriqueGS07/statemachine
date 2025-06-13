from django.db import models
from .product_model import Product
from django.utils import timezone
    
TIME = timezone.now().isoformat()

def initial_state():
    return [{"Pending":{"evento": "CreatedOrder", "hora": TIME}}]

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=250, default="Unkown")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders', default=1)
    amount = models.IntegerField(default=1)
    current_state  = models.CharField(max_length=100, default="Pending")
    state_log = models.JSONField(default=initial_state)
    active_ticket = models.IntegerField(default=-1)
    
    
    

    