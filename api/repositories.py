from .models import Order, Product

#ORDERS
def get_all_orders():
    return Order.objects.all()

def create_order(data):
    if "product" in data:
        try:
            data["product"] = Product.objects.get(pk=data["product"])
        except Product.DoesNotExist:
            raise ValueError(f"Producto con id {data['product']} no existe.")
    return Order.objects.create(**data)

def get_order_by_id(order_id):
    return Order.objects.get(id=order_id)

def delete_order_by_id(order_id):
    Order.objects.filter(id=order_id).delete()

def delete_all_orders():
    Order.objects.all().delete()

#PRODUCTS
def get_all_products():
    return Product.objects.all()

def create_product(data):
    return Product.objects.create(**data)

def get_product_by_id(order_id):
    return Product.objects.get(id=order_id)

def delete_product_by_id(order_id):
    Product.objects.filter(id=order_id).delete()

def delete_all_products():
    Product.objects.all().delete()