from django.contrib import admin
from .models import Product, Ask_Complaint, Review
from .forms import ProductForm, ReviewForm, AskComplaintForm

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = (
        'id',
        'name',
        'categories',
        'price',
        'brand',
        'descriptions',
        'image',
    )
        
    ordering = ('id',)

admin.site.register(Product, ProductAdmin)    

class ReviewAdmin(admin.ModelAdmin):
    form = ReviewForm
    list_display = (
        'text',
        'product',
        'user',
        'created_at',
    )
        
    ordering = ('created_at', )

admin.site.register(Review, ReviewAdmin)    

class AskcomplaintAdmin(admin.ModelAdmin):
    form = AskComplaintForm
    list_display = (
        'user',
        'name',
        'email',
        'topic',
        'detail',
        'created_at',
      
    )
        
    ordering = ('created_at', )

admin.site.register(Ask_Complaint, AskcomplaintAdmin)
