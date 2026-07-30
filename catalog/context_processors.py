from django.db.models import Sum

from .models import (
    Wishlist,
    Category,
    Cart,
)

def global_data(request):

    wishlist_products = []

    wishlist_count = 0
    cart_count = 0

    cart = None
    if request.session.session_key:

        wishlist_products = list(

            Wishlist.objects.filter(

                session_key=request.session.session_key

            ).values_list(

                "product_id",

                flat=True

            )

        )

        wishlist_count = len(wishlist_products)

    if request.user.is_authenticated:

        cart = Cart.objects.filter(
            user=request.user
        ).first()

    else:

        if request.session.session_key:

            cart = Cart.objects.filter(
                session_key=request.session.session_key
            ).first()

    if cart:

        cart_count = (

            cart.items.aggregate(

                total=Sum("quantity")

            )["total"]

            or 0

        )
    categories = Category.objects.filter(
        status=True
    )

    return {

        "wishlist_products": wishlist_products,

        "wishlist_count": wishlist_count,
        "cart_count": cart_count,

        "navbar_categories": categories,

    }
