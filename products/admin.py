from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'categories',
        'price',
        'brand',
        'descriptions',
    )
        
    ordering = ('id',)

admin.site.register(Product, ProductAdmin)
