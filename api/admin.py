from django.contrib import admin
from .models.order_model import Order
from .models.product_model import  Product

# Register your models here.
admin.site.register(Order)
admin.site.register(Product)