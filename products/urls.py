from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.selected_product, name='selected_product'),
    path('add/', views.add_product, name='add_product'),
]
