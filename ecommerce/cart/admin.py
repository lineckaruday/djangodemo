from django.contrib import admin
from cart.models import Cart,Order,Account
from django.http import HttpResponse           #added http just to know this updates in git (git repository project clone ,update)
# Register your models here.

admin.site.register(Cart)       #table name or model name Book

admin.site.register(Order)

admin.site.register(Account)
