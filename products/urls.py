from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('add/', views.add_product, name='add_product'),
    path('ask_complaint/', views.ask_complaint, name='ask_complaint'),
    path('<product_id>/', views.selected_product, name='selected_product'),
    path('edit/<product_id>/', views.edit_product, name='edit_product'),
    path('delete/<product_id>/', views.delete_product, name='delete_product'),
    path('<product_id>/reviews/', views.review_product, name='review_product')
    
]
