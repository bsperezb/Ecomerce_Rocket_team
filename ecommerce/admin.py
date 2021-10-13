from django.contrib import admin
from .models.ecommerce import Item_Artesanias, OrderItem, Order
# Register your models here.

admin.site.register(Item_Artesanias)
admin.site.register(OrderItem)
admin.site.register(Order)
