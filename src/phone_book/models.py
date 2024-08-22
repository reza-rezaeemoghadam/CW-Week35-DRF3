from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)    

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name='contact')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
