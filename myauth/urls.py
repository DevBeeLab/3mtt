from django.urls import path
from .views import *


urlpatterns = [
    path('signup', SignupView.as_view(), name='signup'),
    path('login', LoginView, name='login'),
    path('logout', LogoutView, name='logout'),
]