from django.contrib import admin
from .models import ProductType, Product, Comment

admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Comment)
