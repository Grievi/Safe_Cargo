from django.utils import tree
from app.models import Profile, Cargo
from rest_framework import serializers

class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'
        
class Cargoserializer(serializers.ModelSerializer):
    customer=Profileserializer(many=True, read_only=True)

    class Meta:
        model=Cargo
        fields='__all__'


