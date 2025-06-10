from ..models.order_model import Order
from ..models.product_model import Product

#ORDERS
def get_all_orders():
    return Order.objects.all()

def create_order(data):
    if "product" in data:
        try:
            data["product"] = Product.objects.get(pk=data["product"])
        except Order.DoesNotExist:
            raise ValueError(f"Producto con id {data['product']} no existe.")
        
    return Order.objects.create(**data)

def get_order_by_id(order_id):
    return Order.objects.get(id=order_id)

def delete_order_by_id(order_id):
    Order.objects.filter(id=order_id).delete()

def delete_all_orders():
    Order.objects.all().delete()

