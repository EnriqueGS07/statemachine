from ..repositories import order_repository
from ..models.order_model import Order
from rest_framework.exceptions import NotFound

#ORDERS
def list_orders():
    return order_repository.get_all_orders()

def create_order_service(data):
    if "user" not in data :
        raise ValueError("La orden debe tener un usuario")
    return order_repository.create_order(data)

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
    return order_repository.delete_all_orders()

