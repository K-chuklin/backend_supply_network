from django.contrib import admin
from providers.models import Unit


@admin.register(Unit)
class SupplierAdmin(admin.ModelAdmin):

    list_display = ('pk', 'owner', 'name', 'level', 'country', 'city', 'debt', 'creations_date')
    list_filter = ('level', 'name', 'product', 'country',)
    search_fields = ('level', 'product', 'country')
    actions = ['cleanup_debt']

    def cleanup_debt(self, request, queryset):
        for supply_object in queryset:
            supply_object.debt = 0
            supply_object.save()
        self.message_user(request, f'Задолженность перед поставщиком очищена.')

    cleanup_debt.short_description = 'Очистить задолженность'
