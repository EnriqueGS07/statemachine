from rest_framework import viewsets, response, status, exceptions
from rest_framework.decorators import action
from ..serializers.order_serializer import OrderSerializer
from ..models.order_model import Order
from api.services import order_services

# Create your views here.
#ORDERS
class OrderViewSet(viewsets.ViewSet):
    serializer_class = OrderSerializer
    
    def list(self, request):
        orders = order_services.list_orders()
        serializer = self.serializer_class(orders, many=True)
        return response.Response(serializer.data)
    
    def create(self, request):
        try:
            order = order_services.create_order_service(request.data)
            serializer = self.serializer_class(order)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return response.Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        order = order_services.get_order_by_id(pk)
        if order is None:
            raise exceptions.NotFound("No se encontro la Orden")
        serializer = self.serializer_class(order)
        return response.Response(serializer.data)
    
    def destroy(self, request, pk=None):
            try:
                order_services.delete_order_service(pk)
                return response.Response(status=status.HTTP_204_NO_CONTENT)
            except exceptions.NotFound:
                return response.Response({'error': 'Orden no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['delete'], url_path='delete-all')
    def delete_all_orders(self, request):
        Order.objects.all().delete()
        return response.Response({'message': 'Ordenes Borradas'})
    
    @action (detail=True, methods=['put'], url_path='update-state')
    def update_state(self, request, pk=None):
        order = Order.objects.filter(id=pk).first()
        if not order:
            return response.Response({'error': 'Orden no encontrada'}, status=status.status.HTTP_404_NOT_FOUND)
        trigger = request.data.get('trigger')
        if not trigger:
            return response.Response({'error': 'Seleccione un Trigger'}, status=status.HTTP_400_BAD_REQUEST)
        new_state = order_services.get_new_state(order.current_state, trigger)
        if not new_state:
            return response.Response({'error': "Transicion no valida"}, status=status.HTTP_400_BAD_REQUEST)
        
        order = order_services.update_log(pk, trigger)
        return response.Response({'message':f"Orden '{order.id}' actualizada a '{order.current_state}'"})
    
    
