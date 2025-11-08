from django.db import models
from accounts.models import User
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.conf import settings
from django.contrib.auth import get_user_model


# Create your models here.
def get_user_model_safe():
    try:
        return get_user_model()
    except Exception:
        from django.contrib.auth.models import User
        return User

User = get_user_model_safe()


class Blogs(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    category=models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    status=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    published_at=models.DateTimeField()


    def __str__(self):
        return self.title
    


class Category(models.Model):
    name=models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
    




