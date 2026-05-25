from django.urls import path
from .views import *


urlpatterns = [
    path('products/', Products.as_view(), name='products'),
    path('add-product/', AddProduct.as_view(), name='add-product'),
    path('buy-product/<str:product_id>', buy_product, name='buy-product'),
    path('edit-product/<str:product_id>', EditProduct.as_view(), name='edit-product'),
    path('delete-product/<str:product_id>', delete_product, name='delete-product'),
]