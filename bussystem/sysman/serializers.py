from .models import Destination, TripPath, Bus, User
from rest_framework import serializers

class BusSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, bus):

        if bus.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri('/static/%s' % bus.image.name)
            return '/static/%s' % bus.image.name
    class Meta:
        model = Bus
        fields = '__all__'
class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'

class TripPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripPath
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'avatar']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    def create(self, validated_data):
        data = validated_data.copy()

        user = User(**data)
        user.set_password(data['password'])
        user.save()

        return user