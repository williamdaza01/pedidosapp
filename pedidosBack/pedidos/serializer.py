from rest_framework import serializers
from .models import User, Order, OrderState, Product, ShippingRule

class OrderStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderState
        fields = '__all__'
        
class ShippingRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingRule
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
