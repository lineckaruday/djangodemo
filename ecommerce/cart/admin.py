from django.contrib import admin
from cart.models import Cart,Order,Account
# Register your models here.

admin.site.register(Cart)       #table name or model name Book

admin.site.register(Order)

admin.site.register(Account)
