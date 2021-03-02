from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all product, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)



def selected_product(request, product_id):
    """ A view to show selected product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'products': products,
    }

    return render(request, 'products/selected_product.html', context)