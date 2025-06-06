from rest_framework import viewsets, response, status, exceptions
from rest_framework.decorators import api_view
from .serializers import OrderSerializer, ProductSerializer
from .models import Order, Product
from . import services

# Create your views here.
#ORDERS
class OrderViewSet(viewsets.ViewSet):
    serializer_class = OrderSerializer
    
    def list(self, request):
        orders = services.list_orders()
        serializer = self.serializer_class(orders, many=True)
        return response.Response(serializer.data)
    
    def create(self, request):
        try:
            order = services.create_order_service(request.data)
            serializer = self.serializer_class(order)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return response.Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        order = services.get_order_by_id(pk)
        if order is None:
            raise exceptions.NotFound("No se encontro la Orden")
        serializer = self.serializer_class(order)
        return response.Response(serializer.data)
    
    def destroy(self, request, pk=None):
        services.delete_order_service(pk)
        return response.Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def delete_all_orders(request):
    Order.objects.all().delete()
    return response.Response({'message': 'All orders deleted.'})

#PRODUCTS
class ProductViewSet(viewsets.ViewSet):
    serializer_class = ProductSerializer
    
    def list(self, request):
        products = services.list_products()
        serializer = self.serializer_class(products, many=True)
        return response.Response(serializer.data)
    
    def create(self, request):
        try:
            product = services.create_product_service(request.data)
            serializer = self.serializer_class(product)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return response.Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        product = services.get_product_by_id(pk)
        if product is None:
            raise exceptions.NotFound("No se encontro la Orden")
        serializer = self.serializer_class(product)
        return response.Response(serializer.data)

    def destroy(self, request, pk=None):
        try:
            services.delete_product_service(pk)
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except exceptions.NotFound:
            return response.Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_all_products(request):
    Product.objects.all().delete()
    return response.Response({'message': 'All Products deleted.'})