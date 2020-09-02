from django.contrib import admin
from .models import Category,Product,Brand,ProductImages,Location,Seller

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductImages)
admin.site.register(Location)
admin.site.register(Seller)
# Register your models here.
