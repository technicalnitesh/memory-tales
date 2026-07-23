from catalog.models import Category, Product


PRODUCTS = [
    {
        "category": "Photo Frames",
        "name": "Classic Black Frame",
        "slug": "classic-black-frame",
        "sku": "PF001",
        "price": 799,
        "featured": True,
    },
    {
        "category": "Photo Frames",
        "name": "Premium White Frame",
        "slug": "premium-white-frame",
        "sku": "PF002",
        "price": 999,
        "featured": True,
    },
    {
        "category": "Photo Frames",
        "name": "Luxury Golden Frame",
        "slug": "luxury-golden-frame",
        "sku": "PF003",
        "price": 1499,
        "featured": False,
    },
    {
        "category": "Canvas Prints",
        "name": "Canvas Print 12x18",
        "slug": "canvas-print-12x18",
        "sku": "CP001",
        "price": 699,
        "featured": True,
    },
    {
        "category": "Canvas Prints",
        "name": "Canvas Print 18x24",
        "slug": "canvas-print-18x24",
        "sku": "CP002",
        "price": 1199,
        "featured": True,
    },
    {
        "category": "Photo Albums",
        "name": "Wedding Album",
        "slug": "wedding-album",
        "sku": "PA001",
        "price": 2499,
        "featured": True,
    },
    {
        "category": "Photo Albums",
        "name": "Baby Memory Album",
        "slug": "baby-memory-album",
        "sku": "PA002",
        "price": 1999,
        "featured": False,
    },
    {
        "category": "Photo Mugs",
        "name": "Magic Mug",
        "slug": "magic-mug",
        "sku": "PM001",
        "price": 499,
        "featured": True,
    },
    {
    "category": "Photo Albums",
    "name": "Wedding Album",
    "slug": "wedding-album",
    "sku": "PA001",
    "price": 2499,
    "featured": True,
},
{
    "category": "Photo Albums",
    "name": "Baby Memory Album",
    "slug": "baby-memory-album",
    "sku": "PA002",
    "price": 1999,
    "featured": True,
},
{
    "category": "Photo Albums",
    "name": "Travel Album",
    "slug": "travel-album",
    "sku": "PA003",
    "price": 1899,
    "featured": False,
},
{
    "category": "Photo Albums",
    "name": "Birthday Album",
    "slug": "birthday-album",
    "sku": "PA004",
    "price": 1699,
    "featured": False,
},
{
    "category": "Photo Albums",
    "name": "Anniversary Album",
    "slug": "anniversary-album",
    "sku": "PA005",
    "price": 2299,
    "featured": True,
},
{
    "category": "Photo Mugs",
    "name": "Magic Mug",
    "slug": "magic-mug",
    "sku": "PM001",
    "price": 499,
    "featured": True,
},
{
    "category": "Photo Mugs",
    "name": "White Coffee Mug",
    "slug": "white-coffee-mug",
    "sku": "PM002",
    "price": 299,
    "featured": True,
},
{
    "category": "Photo Mugs",
    "name": "Couple Mug Set",
    "slug": "couple-mug-set",
    "sku": "PM003",
    "price": 799,
    "featured": False,
},
{
    "category": "Photo Mugs",
    "name": "Heart Handle Mug",
    "slug": "heart-handle-mug",
    "sku": "PM004",
    "price": 599,
    "featured": False,
},
{
    "category": "Photo Mugs",
    "name": "Travel Mug",
    "slug": "travel-mug",
    "sku": "PM005",
    "price": 899,
    "featured": True,
},
{
    "category": "Calendars",
    "name": "Desk Calendar",
    "slug": "desk-calendar",
    "sku": "CL001",
    "price": 399,
    "featured": False,
},
{
    "category": "Calendars",
    "name": "Wall Calendar",
    "slug": "wall-calendar",
    "sku": "CL002",
    "price": 599,
    "featured": True,
},
{
    "category": "Calendars",
    "name": "Family Calendar",
    "slug": "family-calendar",
    "sku": "CL003",
    "price": 699,
    "featured": False,
},
{
    "category": "Cushions",
    "name": "Square Cushion",
    "slug": "square-cushion",
    "sku": "CU001",
    "price": 699,
    "featured": True,
},
{
    "category": "Cushions",
    "name": "Heart Cushion",
    "slug": "heart-cushion",
    "sku": "CU002",
    "price": 799,
    "featured": True,
},
{
    "category": "Cushions",
    "name": "Round Cushion",
    "slug": "round-cushion",
    "sku": "CU003",
    "price": 749,
    "featured": False,
},
{
        "category": "Canvas Prints",
        "name": "Canvas Print 12x18",
        "slug": "canvas-print-12x18",
        "sku": "CP001",
        "short_description": "Premium HD canvas print for stunning wall decoration.",
        "description": "Turn your favorite photos into beautiful wall art with premium canvas printing. Printed using fade-resistant inks on artist-grade canvas stretched over a durable wooden frame.",
        "price": 699,
        "featured": True,
    },

    {
        "category": "Canvas Prints",
        "name": "Canvas Print 18x24",
        "slug": "canvas-print-18x24",
        "sku": "CP002",
        "short_description": "Large premium canvas print with vibrant color reproduction.",
        "description": "Designed for high-resolution photography, this premium canvas print transforms your memories into gallery-quality artwork suitable for homes, offices, and gifting.",
        "price": 1199,
        "featured": True,
    },

    {
        "category": "Canvas Prints",
        "name": "Large Canvas 24x36",
        "slug": "large-canvas-24x36",
        "sku": "CP003",
        "short_description": "Oversized premium canvas print for modern wall décor.",
        "description": "Create an impressive statement with our 24x36 premium canvas print featuring HD printing, fade-resistant inks, and a strong wooden frame for long-lasting beauty.",
        "price": 1899,
        "featured": True,
    },

    {
        "category": "Canvas Prints",
        "name": "Panorama Canvas",
        "slug": "panorama-canvas",
        "sku": "CP004",
        "short_description": "Wide panorama canvas designed for landscape photography.",
        "description": "Perfect for travel, nature, and cityscape photography, this panoramic canvas print delivers exceptional detail and vibrant colors with premium-quality finishing.",
        "price": 1599,
        "featured": False,
    },

    {
        "category": "Canvas Prints",
        "name": "Square Canvas",
        "slug": "square-canvas",
        "sku": "CP005",
        "short_description": "Modern square canvas print for Instagram-style photos.",
        "description": "Showcase your square-format photos in a premium-quality canvas print designed with vibrant colors, durable construction, and elegant wall presentation.",
        "price": 999,
        "featured": False,
    },
    {
    "category": "Mobile Covers",
    "name": "iPhone Custom Cover",
    "slug": "iphone-custom-cover",
    "sku": "MC001",
    "price": 499,
    "featured": True,
},
{
    "category": "Mobile Covers",
    "name": "Samsung Custom Cover",
    "slug": "samsung-custom-cover",
    "sku": "MC002",
    "price": 499,
    "featured": False,
},
{
    "category": "Mobile Covers",
    "name": "OnePlus Custom Cover",
    "slug": "oneplus-custom-cover",
    "sku": "MC003",
    "price": 549,
    "featured": False,
},
{
    "category": "Cushions",
    "name": "Square Cushion",
    "slug": "square-cushion",
    "sku": "CU001",
    "price": 699,
    "featured": True,
},
{
    "category": "Cushions",
    "name": "Heart Cushion",
    "slug": "heart-cushion",
    "sku": "CU002",
    "price": 799,
    "featured": True,
},
{
    "category": "Cushions",
    "name": "Round Cushion",
    "slug": "round-cushion",
    "sku": "CU003",
    "price": 749,
    "featured": False,
},
{
    "category": "Calendars",
    "name": "Desk Calendar",
    "slug": "desk-calendar",
    "sku": "CL001",
    "price": 399,
    "featured": False,
},
{
    "category": "Calendars",
    "name": "Wall Calendar",
    "slug": "wall-calendar",
    "sku": "CL002",
    "price": 599,
    "featured": True,
},
{
    "category": "Calendars",
    "name": "Family Calendar",
    "slug": "family-calendar",
    "sku": "CL003",
    "price": 699,
    "featured": False,
},
]
def seed_products():

    created = 0

    for item in PRODUCTS:

        category = Category.objects.get(name=item["category"])

        _, is_created = Product.objects.get_or_create(

            sku=item["sku"],

            defaults={

                "category": category,

                "name": item["name"],

                "slug": item["slug"],

                "short_description": item["name"],

                "description": item["name"] + " - Premium Quality Personalized Product",

                "base_price": item["price"],

                "thumbnail": "products/default.jpg",

                "is_featured": item["featured"],

                "status": True,

            }

        )

        if is_created:
            created += 1

    return created