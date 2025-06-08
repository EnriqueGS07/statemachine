from rest_framework import viewsets, response, status, exceptions
from rest_framework.decorators import action
from ..serializers.product_serializer import ProductSerializer
from ..models.product_model import Product
from api.services import product_services


#PRODUCTS
class ProductViewSet(viewsets.ViewSet):
    serializer_class = ProductSerializer
    
    def list(self, request):
        products = product_services.list_products()
        serializer = self.serializer_class(products, many=True)
        return response.Response(serializer.data)
    
    def create(self, request):
        try:
            product = product_services.create_product_service(request.data)
            serializer = self.serializer_class(product)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return response.Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        product = product_services.get_product_by_id(pk)
        if product is None:
            raise exceptions.NotFound("No se encontro la el producto")
        serializer = self.serializer_class(product)
        return response.Response(serializer.data)

    def destroy(self, request, pk=None):
        try:
            
            product_services.delete_product_service(pk)
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except exceptions.NotFound:
            return response.Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['delete'], url_path='delete-all')
    def delete_all_products(self, request):
        Product.objects.all().delete()
        return response.Response({'message': 'Productos borrados.'})