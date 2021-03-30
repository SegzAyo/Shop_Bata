from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm, AskComplaintForm, ReviewForm

# Create your views here.

def all_products(request):
    """ A view to show all product, including sorting and search queries """

    page = request.GET.get('page', 1)

    products = Product.objects.all().order_by('-created_at')
    query = None
    Brand = None
    sort = None
    direction = None
    Categories = None



    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'brand' in request.GET:
            Brand = request.GET['brand']
            products = products.filter(brand=Brand)  

        if 'categories' in request.GET:
            Categories = request.GET['categories']
            products = products.filter(categories=Categories) 

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(descriptions__icontains=query) | Q(categories__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'  

    paginator = Paginator(products, 12)

    try:
        products_paginated = paginator.page(page)
    except PageNotAnInteger:
        products_paginated = paginator.page(1)
    except EmptyPage:
        products_paginated = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'products_paginated': products_paginated,
        'search_term': query,
        'current_brand': Brand,
        'current_sorting': current_sorting,
        'Shoe_categories': Categories
    }

    return render(request, 'products/products.html', context)



def selected_product(request, product_id):
    """ A view to show selected product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        'review_form': ReviewForm()
    }

    return render(request, 'products/selected_product.html', context)

@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        print(request.POST, request.FILES)
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('selected_product', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('selected_product', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))

def ask_complaint(request):
    if request.method == "GET":
        form = AskComplaintForm()

        return render(request, 'products/ask_complaint.html', {'form': form})

    if request.method == 'POST':
        form = AskComplaintForm(request.POST)
        if form.is_valid():
            ask_complaint = form.save()
            messages.success(request, 'Sent successfully!')
        else:
            messages.error(request, 'Please ensure the form is filled correctly!')
        
        return render(request, 'products/ask_complaint.html', {'form': AskComplaintForm()})
    
    return render(request, 'products/ask_complaint.html')


@login_required
@require_POST
def review_product(request, product_id):
    """Review a product"""

    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        redirect_url = request.POST.get('redirect_url')

        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.instance.product = product
            form.save()
            messages.success(request, 'Your review has been submitted')
        else:
            messages.error(request, 'There is an error with your review')

        return redirect(redirect_url)


        
        