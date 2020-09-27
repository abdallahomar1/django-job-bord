import django_filters
from .models import jop
class jobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact')
    description = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = jop
        fields = '__all__'
        exclude = ['image', 'owenr', 'published']