from ..repositories import product_repository
from ..models.product_model import Product
from rest_framework.exceptions import NotFound

#PRODUCTS
def list_products():
    return product_repository.get_all_products()

def create_product_service(data):
    if "name" not in data or "price" not in data :
        raise ValueError("Datos del producto incompletos")
    return product_repository.create_product(data)

def get_product_by_id(product_id):
    try:
        return Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        None
        
def delete_product_service(pk):
    try:
        product = Product.objects.get(pk=pk)
        product.delete()
    except Product.DoesNotExist:
        raise NotFound()
    
def delete_all_orders_service():
    return product_repository.delete_all_products()