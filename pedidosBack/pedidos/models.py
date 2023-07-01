from django.db import models

class OrderState(models.Model):
    class state_choices(models.TextChoices):
        pending= 'Pendiente'
        on_the_way= 'En ruta'
        delivered= 'Entregado'
        cancelled= 'Cancelado'

    state = models.CharField(choices=state_choices.choices, primary_key=True, max_length=255)

    class Meta:
        managed = True
        
class ShippingRule(models.Model):
    class shipping_choices(models.TextChoices):
        delivery = "Domicilio"
        at_point = "Recoge en punto"
        
    shipping_rule = models.CharField(choices=shipping_choices.choices ,primary_key=True, max_length=255)

    class Meta:
        managed = True

class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255, default='N/A')
    
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    price = models.BigIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    date = models.DateField(auto_now_add=True)
    order_state = models.CharField(choices=OrderState.state_choices.choices, default='pending', max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    is_paid = models.BooleanField(default=False)
    shipping_rule = models.CharField(choices=ShippingRule.shipping_choices.choices, default='delivery', max_length=255)
    quantity_product = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
