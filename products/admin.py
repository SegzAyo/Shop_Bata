from django.contrib import admin
from .models import Product
from .forms import ProductForm

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
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
