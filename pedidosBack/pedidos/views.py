from rest_framework import viewsets, mixins, status
from django.http import JsonResponse
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import timedelta
from django.views.decorators.csrf import csrf_exempt
from .serializer import UserSerializer, OrderSerializer, OrderStateSerializer, ProductSerializer, ShippingRuleSerializer
from .models import User, OrderState, Order, Product, ShippingRule

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrderStateViewSet(viewsets.ModelViewSet):
    queryset = OrderState.objects.all()
    serializer_class = OrderStateSerializer

class ShippingRuleViewSet(viewsets.ModelViewSet):
    queryset = ShippingRule.objects.all()
    serializer_class = ShippingRuleSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

@csrf_exempt
def get_orders_number( request):
    if request.method == 'GET':
        orders_number = Order.objects.count()
        print(orders_number)
        data = {'orders_number': orders_number}
        return JsonResponse(data, status=status.HTTP_200_OK)

@csrf_exempt
def get_clients_number( request):
    if request.method == 'GET':
        clients_number = User.objects.count()
        data = {'clients_number': clients_number}
        return JsonResponse(data, status=status.HTTP_200_OK)

@csrf_exempt
def get_income_last_month( request):
    if request.method == 'GET':
        date_mounth = timezone.now() - timedelta(days=30)

        income_last_month = Order.objects.filter(is_paid=True, date__gte=date_mounth).aggregate(total=Sum('product__price'))
        data = {'income_last_month': income_last_month}
        return JsonResponse(data, status=status.HTTP_200_OK)

@csrf_exempt
def get_city_most_orders( request):
    if request.method == 'GET':
        city_most_orders = User.objects.values('city').annotate(num_pedidos=Count('order')).order_by('-num_pedidos').first()
        data = {'city_most_orders': city_most_orders}
        return JsonResponse(data, status=status.HTTP_200_OK)

@csrf_exempt
def get_best_selling_product( request):
    if request.method == 'GET':
        best_selling_product = Order.objects.values('product__name').annotate(total_vendido=Sum('quantity_product')).order_by('-total_vendido').first()
        data = {'best_selling_product': best_selling_product}
        return JsonResponse(data, status=status.HTTP_200_OK)
