# from typing_extensions import Required
from django.db import models
from django.conf import settings

class Item_Artesanias(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete=models.CASCADE)
    item = models.ForeignKey(Item_Artesanias, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.title
    def get_final_price(self):
        return self.quantity * self.item.price

class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    
    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([order_item.get_final_price() for order_item in self.items.all()])


    def __str__(self):
        return self.title
    


