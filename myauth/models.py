from django.db import models

# Create your models here.

class SignupView(models.Model):
    username = models.CharField(max_length=150, unique=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
