from django.db import models
from django.contrib.auth.models import User
from profiles.models import Address
from products.models import Product
from django.conf import settings
class Order(models.Model):
    STATUS_CHOICES = (
        ('Yet to be Delivered', 'Yet to be Delivered'),  # default for new orders
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
      )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="orders")
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Yet to be Delivered')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    payment_method = models.CharField(max_length=20, choices=[("cod", "Cash on Delivery"), ("online", "Online Payment")],default="cod")
    is_paid = models.BooleanField(default=False)  # update when online payment succeeds
    
    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
