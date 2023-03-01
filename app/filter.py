import django_filters
from .models import Work, Artist

class ArtistFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Artist
        fields = ['name']

class WorkFilter(django_filters.FilterSet):
    # artist = django_filters.ModelChoiceFilter(queryset=Artist.objects.all(), field_name='name', to_field_name='id')
    class Meta:
        model = Work
        fields ={
            'work_type': ['exact'],
            'artist': ['exact']
        }
