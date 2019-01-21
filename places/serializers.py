from rest_framework import serializers
from places.models import Place, Rate


class RateSerializer(serializers.ModelSerializer):
    place = serializers.StringRelatedField()
    #place = PlaceSerializer()
    class Meta:
        model = Rate
        fields = ('id','place','rate','review','des_rates')

class PlaceSerializer(serializers.ModelSerializer):
    #rate_set = RateSerializer(many=True,read_only=True)
    rate_set = serializers.StringRelatedField(many=True)
    class Meta:
        model = Place
        #fields = '__all__'
        fields = ('id','name','description','country','image','rate_set')
