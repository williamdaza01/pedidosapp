from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, OrderStateViewSet, ProductViewSet, OrderViewSet, ShippingRuleViewSet, get_best_selling_product, get_city_most_orders, get_clients_number, get_income_last_month, get_orders_number

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('order-states', OrderStateViewSet)
router.register('shipping-rules', ShippingRuleViewSet)
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('orders/orders-number', get_orders_number),
    path('orders/clients-number', get_clients_number),
    path('orders/income-last-month', get_income_last_month),
    path('orders/city-most-orders', get_city_most_orders),
    path('orders/best-selling-product', get_best_selling_product),
]
