from . import repositories
from .models import Order, Product
from rest_framework.exceptions import NotFound

#ORDERS
def list_orders():
    return repositories.get_all_orders()

def create_order_service(data):
    if "user" not in data :
        raise ValueError("La orden debe tener un usuario")
    return repositories.create_order(data)

def get_order_by_id(order_id):
    try:
        return Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        None
        
def delete_order_service(pk):
    try:
        order = Order.objects.get(pk=pk)
        order.delete()
    except Order.DoesNotExist:
        raise NotFound()

def delete_all_orders_service():
    return repositories.delete_all_orders()

#PRODUCTS
def list_products():
    return repositories.get_all_products()

def create_product_service(data):
    if "name" not in data or "price" not in data :
        raise ValueError("Datos del producto incompletos")
    return repositories.create_product(data)

def get_product_by_id(product_id):
    try:
        return Product.objects.get(pk=product_id)
    except Order.DoesNotExist:
        None
        
def delete_product_service(pk):
    try:
        product = Product.objects.get(pk=pk)
        product.delete()
    except Product.DoesNotExist:
        raise NotFound()
def delete_all_orders_service():
    return repositories.delete_all_products()