from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class WardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warden
        fields = "__all__"