from django.contrib import admin
from .models import (
    Category,
    Product,
    ProductImage,
    OptionMaster,
    ProductOption,
    ProductOptionValue,
    Wishlist,
    Cart,
    CartItem,
    CartItemOption,
    CartItemImage,
)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'slug',
        'status',
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'name',
        'slug',
    )

    ordering = (
        'name',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }

class ProductImageInline(admin.TabularInline):

    model = ProductImage

    extra = 1

    fields = (
        'image',
        'alt_text',
        'is_primary',
        'sort_order',
        'status',
    )
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'category',
        'sku',
        'base_price',
        'is_featured',
        'status',
    )

    list_filter = (
        'category',
        'status',
        'is_featured',
    )

    search_fields = (
        'name',
        'sku',
        'slug',
    )

    ordering = (
        'name',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }
    inlines = [ProductImageInline]
@admin.register(OptionMaster)
class OptionMasterAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'field_type',
        'status',
    )

    list_filter = (
        'field_type',
        'status',
    )

    search_fields = (
        'name',
    )

    ordering = (
        'name',
    )
@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'product',
        'option',
        'is_required',
        'status',
        'sort_order',
    )

    list_filter = (
        'status',
        'is_required',
    )

    search_fields = (
        'product__name',
        'option__name',
    )

    ordering = (
        'product',
        'sort_order',
    )
@admin.register(ProductOptionValue)
class ProductOptionValueAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'product_option',
        'value',
        'price',
        'status',
        'sort_order',
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'value',
    )

    ordering = (
        'product_option',
        'sort_order',
    )
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "session_key",
        "product",
        "created_at",
    )

    search_fields = (
        "session_key",
        "product__name",
    )

    list_filter = (
        "created_at",
    )
class CartItemOptionInline(admin.TabularInline):

    model = CartItemOption

    extra = 0

    readonly_fields = (
        "product_option",
        "product_option_value",
        "extra_price",
    )

    can_delete = False
class CartItemImageInline(admin.TabularInline):

    model = CartItemImage

    extra = 0

    readonly_fields = (
    "image",
    "alt_text",
    "created_at",
    )

    can_delete = False
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):

    list_display = (
    "id",
    "cart",
    "product",
    "quantity",
    "unit_price",
    "total_price",
    "created_at",
    )

    list_filter = (
        "created_at",
    )
    readonly_fields = (
    "item_key",
    "created_at",
    "updated_at",
    )

    search_fields = (
        "product__name",
        "item_key",
    )

    inlines = [
        CartItemOptionInline,
        CartItemImageInline,
    ]
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

   
    list_display = (
    "id",
    "user",
    "session_key",
    "cart_items",
    "created_at",
    "updated_at",
    )

    search_fields = (
    "session_key",
    "user__username",
    )
    readonly_fields = (
    "created_at",
    "updated_at",
    )

    list_filter = (
        "created_at",
    )
    def cart_items(self, obj):

        return obj.items.count()

        cart_items.short_description = "Items"
    