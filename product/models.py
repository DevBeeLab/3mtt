from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveBigIntegerField()
    quantity = models.PositiveIntegerField()
    sold = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class  ProductTransactions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='transactions')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='transactions')
    price = models.PositiveBigIntegerField()
    quantity = models.PositiveIntegerField()
    quantity_left = models.PositiveIntegerField()
    sold = models.PositiveIntegerField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    