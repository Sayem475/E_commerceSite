from django.contrib import admin
from .models import category, product, customer

# Register your models here.
admin.site.register((category,product,customer))