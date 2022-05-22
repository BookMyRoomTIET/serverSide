from rest_framework import serializers
from .models import *

class WardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warden
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    extra = StudentSerializer(source='student',read_only=True)
    class Meta:
        model = User
        fields = ["uuid","password","last_login","email","registration_id","phone","name","is_warden","is_staff","created_at","hostel","extra"]