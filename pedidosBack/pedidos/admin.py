from django.contrib import admin
from .models import OrderState, ShippingRule, User, Product, Order

admin.site.register(OrderState)
admin.site.register(ShippingRule)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
