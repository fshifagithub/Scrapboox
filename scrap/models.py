from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class scraps(models.Model):
    name=models.CharField(max_length=200,unique=True)
    category=models.CharField(max_length=200)
    price=models.IntegerField()
    description=models.CharField(max_length=500,null=True,blank=True)
    location=models.CharField(max_length=200)
    priority=models.IntegerField(default=0)
    picture=models.ImageField(upload_to="images",null=True)
    phone_no=models.CharField(max_length=200,null=True)
    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)python managr

    def __str__(self):
        return self.name
    

class UserProfile(models.Model):
    name=models.CharField(max_length=200)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    email=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
  
class Order(models.Model):
    name = models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(scraps,related_name="CartItem")

class WishList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="user_wishlist")
    scrap=models.ManyToManyField(scraps,related_name="wished_scrap")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ','.join(str(item) for item in self.scrap.all())

