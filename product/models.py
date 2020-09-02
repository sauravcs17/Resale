from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings




# Create your models here.

class Product(models.Model):

    CONDITION_TYPE=(

        ("New","New"),
        ("Used","Used")
                    )
    name=models.CharField(max_length=100)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    #owner=UserForeignKey(auto_user_add=True,null=True)
    description=models.TextField(max_length=500)
    
    condition=models.CharField(max_length=100,choices=CONDITION_TYPE)
    image = models.ImageField(upload_to='media/main_products/', blank=True,null=True)
    price=models.CharField(max_length=10)
    created=models.DateTimeField(default=timezone.now)
    category=models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    slug=models.SlugField(blank=True,null=True)
    
    Phone=models.CharField(max_length=10,null=True)
    location=models.ForeignKey('Location',on_delete=models.SET_NULL,null=True)
    email=models.CharField(max_length=500,null=True)

 
    def save(self,*args,**kwargs):
        if not self.slug and self.name:
            self.slug=slugify(self.name)
        super(Product,self).save(*args,**kwargs)

    def __str__(self):
        return self.name



class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    FILE = models.FileField(upload_to='products/', blank=True, null=True)

    class Meta:
        verbose_name='Product Image'
        verbose_name_plural='Product Images'

    def __str__(self):
        return self.product.name



class Category(models.Model):
    #for product catogory
    category_name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='category/',blank=True,null=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self,*args,**kwargs):
        if not self.slug and self.category_name:
            self.slug=slugify(self.category_name)
        super(Category,self).save(*args,**kwargs)



    class Meta:
        verbose_name='category'
        verbose_name_plural='catogories'






    def __str__(self):
        return self.category_name


class Brand(models.Model):
    #for product catogory
    brand_name=models.CharField(max_length=50)
    def __str__(self):
        return self.brand_name


class Location(models.Model):
    location=models.CharField(max_length=20)
    def __str__(self):
        return self.location


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.IntegerField(null=True)


    def __str__(self):
        return self.user.username
