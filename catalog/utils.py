import hashlib


def get_session_key(request):

    if not request.session.session_key:

        request.session.create()

    return request.session.session_key
def generate_item_key(
    product_id,
    quantity,
    options
):

    raw = f"{product_id}-{quantity}"

    for key in sorted(options.keys()):

        raw += f"-{key}:{options[key]}"

    return hashlib.sha256(
        raw.encode()
    ).hexdigest()