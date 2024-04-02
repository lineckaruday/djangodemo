from django.contrib import admin
from shop.models import Category,Product            #imported book.model table from Book app


# Register your models here.

admin.site.register(Category)       #table name or model name Book

admin.site.register(Product)
