from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.TextField()
    subtitle = models.CharField(max_length=500)
    image= models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)