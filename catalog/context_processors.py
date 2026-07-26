from .models import Wishlist, Category
from .models import Cart, CartItem


def global_data(request):

    wishlist_products = []

    wishlist_count = 0

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

    categories = Category.objects.filter(
        status=True
    )

    return {

        "wishlist_products": wishlist_products,

        "wishlist_count": wishlist_count,

        "navbar_categories": categories,

    }
def cart_data(request):

    count = 0

    session_key = request.session.session_key

    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    cart = Cart.objects.filter(
        session_key=session_key
    ).first()

    if cart:

        count = cart.items.count()

    return {
        "cart_count": count
    }