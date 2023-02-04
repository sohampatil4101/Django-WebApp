from bdata.models import BusLoc, Bus, Route, BPoint
from rest_framework import serializers

class BusLocSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusLoc
        fields = ['id','bus', 'lat', 'long']

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ['id','bno','driver','conducter','route','status']

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id','source', 'destination']

class BPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = BPoint
        fields = ['id','route', 'name', 'code', 'lat', 'long']