from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('about/', aboutpage, name='about'),
    # path('contact/', contactpage, name='contact'),
    path('contact/', ContactView.as_view(), name='contact'),
]