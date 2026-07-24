from django.shortcuts import render
from .models import Category, Product
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

def product_list(request):

    products = Product.objects.filter(
        status=True
    ).order_by('-id')

    return render(
        request,
        'catalog/product_list.html',
        {
            'products': products
        }
    )
def about(request):

    return render(
        request,
        'catalog/about.html'
    )


def contact(request):

    return render(
        request,
        'catalog/contact.html'
    )

def product_detail(request, slug):

    product = get_object_or_404(
        Product.objects.prefetch_related(
            "images",
            "options__values",
            "options__option",
        ),
        slug=slug,
        status=True,
    )

    related_products = Product.objects.filter(
        category=product.category,
        status=True
    ).exclude(id=product.id)[:4]

    context = {
        "product": product,
        "related_products": related_products,
    }

    return render(request, "catalog/product_detail.html", context)