from django.shortcuts import render
from .models import Category, Product
from .models import Product
from django.shortcuts import render, get_object_or_404

def home(request):

    categories = Category.objects.filter(status=True)

    featured_products = (
        Product.objects
        .filter(status=True, is_featured=True)
        .select_related('category')
        .prefetch_related('images')
        [:8]
    )

    context = {
        "categories": categories,
        "featured_products": featured_products,
    }

    return render(request, "catalog/home.html", context)

def product_detail(request, slug):

    product = get_object_or_404(
        Product,
        slug=slug,
        status=True
    )

    context = {
        "product": product,
    }

    return render(
        request,
        "catalog/product_detail.html",
        context
    )