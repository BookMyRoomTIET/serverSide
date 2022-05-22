from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from hostel import serializers
from user.custompermissions import *
from rest_framework.permissions import IsAuthenticated
from user.models import *
from .forms import *

class hostelInfoView(APIView):
    def get(self, request, fromat=None):
        hostels = hostelInformationModel.objects.all()
        info_serializer = hostelInformationSerializer(hostels, many=True)
        return Response(info_serializer.data)

class specificHostelView(APIView):
    def post(self, request):
        hostel_id = request.data["hostel_id"]
        hostel = hostelInformationModel.objects.get(hostel_id=hostel_id)
        info_serializer = hostelInformationSerializer(hostel)
        result = info_serializer.data
        return Response(result)

class hostelAllocatedToYearView(APIView):
    def get(self, request, format=None):
        info = hostelAllocatedToYear.objects.all()
        info_serializer = hostelAllocatedToYearSerializer(info, many=True)
        return Response(info_serializer.data)

class availableHostelsView(APIView):
    permission_classes = (IsAuthenticated,isStudent)
    def get(self, request, format=None):
        userYear = request.user.student.grad_year
        sex = request.user.student.sex
        info = hostelAllocatedToYear.objects.filter(gradYear=userYear).filter(gender=sex)
        serializer = hostelAllocatedToYearSerializer(info, many=True)
        return Response(serializer.data)

class preferenceFormView(APIView):
    permission_classes=(IsAuthenticated,isStudent)
    def post(self, request):
        user = request.user
        userYear = user.student.grad_year
        if userYear==2025:
            form = hostelPreferenceFirstYearForm(request.data)
            if form.is_valid():
                form.save()
                return Response({"detail": "Preference saved"})
            else:
                return Response({"detail": "failed", "errors": form.errors}, status=400)
        else:
            form = hostelPreferenceSecondYearForm(request.data)
            if form.is_valid():
                form.save()
                return Response({"detail": "Preference saved"})
            else:
                return Response({"detail": "failed", "errors": form.errors}, status=400)

class roomInformationView(APIView):
    def get(self, request, fromat=None):
        rooms = RoomInformationModel.objects.all()
        room_serializer = hostelRoomSerializer(rooms, many=True)
        return Response(room_serializer.data)