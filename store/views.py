from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_all(request):    
    data_products = Product.products.all()
    return render(request, 'store/index.html', {'products': data_products})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category ,slug=category_slug)
    products = Product.products.filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'products': products})

def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'store/single.html', {'product': product})



