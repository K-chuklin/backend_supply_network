import django_filters
from providers.models import Unit


class UnitFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Unit
        fields = ['city']
