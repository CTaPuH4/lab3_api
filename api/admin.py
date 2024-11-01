from django.contrib import admin

from api.models import Category, Item


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    list_editable = (
        'name',
    )
    search_fields = ('name',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'category',
        'is_published',
    )
    list_editable = (
        'name',
        'price',
        'category',
        'is_published',
    )
    list_filter = (
        'category',
    )
