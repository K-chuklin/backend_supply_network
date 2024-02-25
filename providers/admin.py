from django.contrib import admin
from providers.models import Unit, Products

# admin.site.register(Unit)
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(Products)
