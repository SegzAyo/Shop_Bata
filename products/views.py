from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all product, including sorting and search queries """

    products = Product.objects.all()
    query = None
    Brand = None

    if request.GET:
        if 'brand' in request.GET:
            Brand = request.GET['brand']
            products = products.filter(brand=Brand)  

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(descriptions__icontains=query) | Q(categories__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_brand': Brand,
    }

    return render(request, 'products/products.html', context)



def selected_product(request, product_id):
    """ A view to show selected product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/selected_product.html', context)