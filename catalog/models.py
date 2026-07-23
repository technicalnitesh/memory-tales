from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(
    upload_to='category/',
    blank=True,
    null=True
)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    sku = models.CharField(max_length=50, unique=True)

    short_description = models.CharField(max_length=255)
    description = models.TextField()

    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    thumbnail = models.ImageField(upload_to='products/')

    is_featured = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class OptionMaster(models.Model):

    FIELD_TYPES = (
        ('select', 'Dropdown'),
        ('radio', 'Radio Button'),
        ('checkbox', 'Checkbox'),
        ('text', 'Text Box'),
        ('textarea', 'Textarea'),
        ('number', 'Number'),
        ('image', 'Image Upload'),
    )

    name = models.CharField(max_length=100, unique=True)

    field_type = models.CharField(
        max_length=20,
        choices=FIELD_TYPES,
        default='select'
    )

    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class ProductOption(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='options'
    )

    option = models.ForeignKey(
        OptionMaster,
        on_delete=models.CASCADE,
        related_name='product_options'
    )

    is_required = models.BooleanField(default=True)

    sort_order = models.PositiveIntegerField(default=0)

    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name} - {self.option.name}"
class ProductOptionValue(models.Model):

    product_option = models.ForeignKey(
        ProductOption,
        on_delete=models.CASCADE,
        related_name='values'
    )

    value = models.CharField(max_length=100)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )

    status = models.BooleanField(default=True)

    sort_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product_option} - {self.value}"

    class Meta:
        ordering = ['sort_order', 'value']
class ProductImage(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(
        upload_to='products/gallery/'
    )

    alt_text = models.CharField(
        max_length=200,
        blank=True
    )

    is_primary = models.BooleanField(default=False)

    sort_order = models.PositiveIntegerField(default=0)

    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name} Image"

    class Meta:
        ordering = ['sort_order']