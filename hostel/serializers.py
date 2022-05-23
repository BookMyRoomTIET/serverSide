from rest_framework import serializers
from . import models
from .models import hostelAllocatedToYear

class hostelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.hostelImagesModel
        fields = ["link"]

class hostelMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.hostelMapModel
        fields = ["mapLink"]

class hostelInformationSerializer(serializers.ModelSerializer):
    hostelImage = hostelImagesSerializer(source='hostelimagesmodel_set',many=True,read_only=True)
    hostelMap = hostelMapSerializer(source='hostelmapmodel_set',many=True,read_only=True)
    class Meta:
        model = models.hostelInformationModel
        fields = ["hostel_id","hostelName","hostel_type","warden_name","contact_number","contact_email","description","hostelImage","hostelMap"]

class hostelAllocatedToYearSerializer(serializers.ModelSerializer):
    hostel_id = hostelInformationSerializer(many=False)
    class Meta:
        model = models.hostelAllocatedToYear
        fields = ["hostel_id","gradYear","gender","hostel_id"]

class hostelRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RoomInformationModel
        fields = ['hostel_id','room_id','room_type','room_status','room_capacity','room_price']