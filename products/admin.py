from django.contrib import admin
from products.models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'model', 'release_data')
    list_filter = ('name', 'owner',)
    search_fields = ('name',)
