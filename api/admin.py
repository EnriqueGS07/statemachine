from django.contrib import admin
from .models.models import Order, Product

# Register your models here.
admin.site.register(Order)
admin.site.register(Product)