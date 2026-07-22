from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'parent',
        'status',
        'sort_order',
        'created_at'
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'name',
        'slug'
    )

    ordering = (
        'sort_order',
        'name'
    )

    prepopulated_fields = {
        'slug': ('name',)
    }