from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from places.models import Place, Rate
from places.serializers import PlaceSerializer, RateSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class PlacesViewSet(ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class RatesViewSet(ModelViewSet):
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('place__name','rate','review')
    search_fields = ('place__name','rate','review')
    ordering_fields = '__all__'
    ordering = ('-id',)
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
