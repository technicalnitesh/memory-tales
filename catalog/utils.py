import hashlib

from .models import Cart


def get_session_key(request):
    """
    Session key create karke return karega.
    """

    if not request.session.session_key:
        request.session.create()

    return request.session.session_key


def get_or_create_cart(request):
    """
    Guest/User ke liye cart return karega.
    """

    if request.user.is_authenticated:

        cart, created = Cart.objects.get_or_create(
            user=request.user
        )

    else:

        session_key = get_session_key(request)

        cart, created = Cart.objects.get_or_create(
            session_key=session_key
        )

    return cart


def generate_item_key(product_id, option_ids):
    """
    Product + Selected Options ke basis par unique key banayega.
    """

    option_ids = sorted(option_ids)

    key = f"{product_id}-{'-'.join(map(str, option_ids))}"

    return hashlib.md5(key.encode()).hexdigest()