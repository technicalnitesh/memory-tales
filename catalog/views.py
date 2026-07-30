from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Count
from .models import Wishlist
from django.db.models import Sum


from decimal import Decimal

from django.db import transaction

from django.views.decorators.http import require_POST

from .utils import (
    get_or_create_cart,
    generate_item_key,
)
from .models import (
    Category,
    Product,
    ProductImage,
    Wishlist,
    Cart,
    CartItem,
    CartItemOption,
    CartItemImage,
    ProductOption,
    ProductOptionValue,
)
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
def toggle_wishlist(request):

    if request.method != "POST":

        return JsonResponse({

            "success": False

        })

    product_id = request.POST.get("product_id")

    if not request.session.session_key:

        request.session.create()

    session_key = request.session.session_key

    wishlist = Wishlist.objects.filter(

        session_key=session_key,

        product_id=product_id

    ).first()

    if wishlist:

        wishlist.delete()

        added = False

    else:

        Wishlist.objects.create(

            session_key=session_key,

            product_id=product_id

        )

        added = True

    count = Wishlist.objects.filter(

        session_key=session_key

    ).count()

    return JsonResponse({

        "success": True,

        "added": added,

        "count": count

    })
def wishlist(request):

    if not request.session.session_key:

        request.session.create()

    wishlist = Wishlist.objects.filter(

        session_key=request.session.session_key

    ).select_related(

        "product"

    ).prefetch_related(

        "product__images"

    )

    context = {

    "wishlist": wishlist,

    "page_title": "My Wishlist",

    "page_description":
        "Save your favourite products and purchase them anytime.",

    }

    return render(

        request,

        "catalog/wishlist.html",

        context

    )


@require_POST
@transaction.atomic
def add_to_cart(request):

    cart = get_or_create_cart(request)

    product_id = request.POST.get("product_id")

    quantity = int(
        request.POST.get(
            "quantity",
            1
        )
    )

    try:

        product = Product.objects.get(
            id=product_id,
            status=True
        )

    except Product.DoesNotExist:

        return JsonResponse({

            "success": False,

            "message": "Product not found."

        })
    selected_values = request.POST.getlist("options")

    option_ids = []

    option_total = Decimal("0.00")

    for value_id in selected_values:

        try:

            option = ProductOptionValue.objects.select_related(
                "product_option"
            ).get(
                id=value_id,
                status=True
            )

            option_ids.append(option.id)

            option_total += option.price

        except ProductOptionValue.DoesNotExist:

            continue


    item_key = generate_item_key(

            product.id,

            option_ids

        )
    unit_price = product.base_price + option_total

    cart_item = CartItem.objects.filter(
        cart=cart,
        item_key=item_key
    ).first()

    if cart_item:

        cart_item.quantity += quantity

        cart_item.total_price = (
            cart_item.quantity * unit_price
        )

        cart_item.save()

        return JsonResponse({

            "success": True,

            "message": "Cart updated.",

            "count": cart.items.count()

        })
    cart_item = CartItem.objects.create(

        cart=cart,

        product=product,

        quantity=quantity,

        unit_price=unit_price,

        total_price=unit_price * quantity,

        item_key=item_key

    )
    for value_id in selected_values:

        try:

            option = ProductOptionValue.objects.select_related(
                "product_option"
            ).get(
                id=value_id,
                status=True
            )

            CartItemOption.objects.create(

                cart_item=cart_item,

                product_option=option.product_option,

                product_option_value=option,

                extra_price=option.price

            )

        except ProductOptionValue.DoesNotExist:

            continue
    uploaded_image = request.FILES.get("uploaded_image")

    if uploaded_image:

        CartItemImage.objects.create(

            cart_item=cart_item,

            image=uploaded_image,

            alt_text=product.name

        )
    return JsonResponse({

    "success": True,

    "message": "Product added to cart.",

    "count": cart.items.count()

    })

from django.db.models import Sum

def cart(request):

    if request.user.is_authenticated:

        cart = Cart.objects.filter(
            user=request.user
        ).first()

    else:

        if not request.session.session_key:

            request.session.create()

        cart = Cart.objects.filter(
            session_key=request.session.session_key
        ).first()

    cart_items = []

    grand_total = 0

    if cart:

        cart_items = (

            cart.items
            .select_related("product")
            .prefetch_related(
                "options__product_option",
                "options__product_option_value",
                "images",
            )

        )

        grand_total = (

            cart_items.aggregate(

                total=Sum("total_price")

            )["total"]

            or 0

        )

    context = {

        "cart": cart,

        "cart_items": cart_items,

        "grand_total": grand_total,

    }

    return render(

        request,

        "catalog/cart.html",

        context,

    )