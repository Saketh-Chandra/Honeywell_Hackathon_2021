import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class objectfilter(django_filters.FilterSet):
    description = CharFilter(field_name='description', lookup_expr='icontains')
    title = CharFilter(field_name='title',lookup_expr='icontains')
    class Meta:
        model = Object
        fields=['ObjectID']