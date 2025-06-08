from rest_framework import serializers
from ..models.order_model import Order

class OrderSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    class Meta:
        model = Order
        fields='__all__'
        
