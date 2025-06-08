from ..models.product_model import Product

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