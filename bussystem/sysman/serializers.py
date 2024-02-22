from .models import Destination, TripPath
from rest_framework import serializers


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'

class TripPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripPath
        fields = '__all__'

