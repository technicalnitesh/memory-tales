from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Count
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
def product_list(request):

    products = Product.objects.filter(
        status=True
    ).select_related(
        "category"
    ).prefetch_related(
        "images"
    )
    search = request.GET.get(
    "search"
    )
    category = request.GET.get("category")

    if category:

        products = products.filter(

            category__slug=category

        )

    if search:
        products = products.filter(
            name__icontains=search
        )
    sort = request.GET.get("sort")

    if sort == "price_low":

        products = products.order_by("base_price")

    elif sort == "price_high":

        products = products.order_by("-base_price")

    elif sort == "name_asc":

        products = products.order_by("name")

    elif sort == "name_desc":

        products = products.order_by("-name")

    else:

        products = products.order_by("-id")

    categories = Category.objects.filter(
    status=True
    ).annotate(
        product_count=Count("products")
    ).filter(
        product_count__gt=0
    )
    category_slug = request.GET.get("category")

    page_title = "All Products"

    if category_slug:

        category = Category.objects.filter(
            slug=category_slug,
            status=True
        ).first()

    if category:

        page_title = category.name


# -------------------------
# Price Filter
# -------------------------

    min_price = request.GET.get("min_price")

    max_price = request.GET.get("max_price")

    if min_price:

        products = products.filter(
            base_price__gte=min_price
        )

    if max_price:

        products = products.filter(
            base_price__lte=max_price
        )
    # Pagination

    paginator = Paginator(products, 12)

    page = request.GET.get("page")

    products = paginator.get_page(page)

    context = {

        "page_title": page_title,

        "products": products,

        "categories": categories,
        "selected_category": category_slug,

    }

    if request.headers.get("x-requested-with") == "XMLHttpRequest":

        html = render_to_string(

            "catalog/components/product-content.html",

            context,

            request=request
        )

        return JsonResponse({

            "html": html

        })

    return render(

        request,

        "catalog/product_list.html",

        context

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

def category_products(request, slug):

    category = get_object_or_404(

        Category,

        slug=slug,

        status=True

    )

    products = Product.objects.filter(

        category=category,

        status=True

    ).select_related(

        "category"

    ).prefetch_related(

        "images"

    )

    categories = Category.objects.filter(

        status=True

    )
    search = request.GET.get(
    "search"
    )

    if search:

        products = products.filter(

            name__icontains=search

        )
    sort = request.GET.get("sort")

    if sort == "price_low":

        products = products.order_by("base_price")

    elif sort == "price_high":

        products = products.order_by("-base_price")

    elif sort == "name_asc":

        products = products.order_by("name")

    elif sort == "name_desc":

        products = products.order_by("-name")

    else:

        products = products.order_by("-id")

    context = {

        "page_title": category.name,

        "products": products,

        "categories": categories,

    }

    if request.headers.get("x-requested-with") == "XMLHttpRequest":

        html = render_to_string(

            "catalog/components/product-content.html",

            context,

            request=request
        )

    return JsonResponse({

        "html": html

    })

    return render(

        request,

        "catalog/product_list.html",

        context

    )