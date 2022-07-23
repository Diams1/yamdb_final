from django_filters.rest_framework import CharFilter, FilterSet

from titles.models import Title


class TitleFilter(FilterSet):
    genre = CharFilter(field_name='genre__slug', )
    category = CharFilter(field_name='category__slug', )
    name = CharFilter(field_name='name', lookup_expr='contains', )

    class Meta:
        model = Title
        fields = ['year']
