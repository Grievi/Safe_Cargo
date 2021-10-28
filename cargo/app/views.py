
from app.models import Profile, Cargo
from app.serializers import Profileserializer, Cargoserializer
from rest_framework import viewsets

class CargoApi(viewsets.ModelViewSet):

    queryset=Cargo.objects.all()
    serializer_class=Cargoserializer


class ProfileApi(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=Profileserializer


