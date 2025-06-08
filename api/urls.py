from django.urls import path, include
from rest_framework import routers
from .views.order_views import OrderViewSet
from .views.product_views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet, basename="order")
router.register(r'products', ProductViewSet, basename='product')


urlpatterns=[
    #path('orders/delete_all/', delete_all_orders, name='delete-all-orders'),
    #path('products/delete_all/', delete_all_products, name='delete-all-orders'),
    path('', include(router.urls)),
]