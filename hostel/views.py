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

a_capacity = 300
c_capacity = 300
h_capacity = 300
j_capacity = 300
e_capacity = 300
g_capacity = 300
i_capacity = 300
pg_capacity = 300

class allocationAlgoView(APIView):
    def get(self,request):
        if request.user.student.grad_year==2025:
            sortedcgpa= hostelPreferenceFirstYear.objects.name.order_by('cgpa')
            for i in sortedcgpa:
                stud = User.objects.get(name=i)
                if stud.sex=="Male":
                    if i.preferenceOne=="A":
                        if a_capacity>0:
                            i.hostel = "A"
                            a_capacity = a_capacity-1
                        else:
                            i.hostel = "C"
                            c_capacity = c_capacity-1
                    else:
                        if c_capacity>0:
                            i.hostel = "C"
                            c_capacity = c_capacity-1
                        else:
                            i.hostel = "A"
                            a_capacity = a_capacity-1    
                else:
                    if i.user.preferenceOne=="E":
                        if e_capacity>0:
                            i.hostel = "E"
                            e_capacity = e_capacity-1
                        else:
                            i.hostel = "G"
                            g_capacity = g_capacity-1
                    else:
                        if g_capacity>0:
                            i.hostel = "G"
                            g_capacity = g_capacity-1
                        else:
                            i.hostel = "E"
                            e_capacity = e_capacity-1
        else:
            sortedcgpa= hostelPreferenceSecondYear.objects.order_by('cgpa')
            for i in sortedcgpa:
                if i.sex=="Male":
                    if i.preferenceOne=="J":
                        if j_capacity>0:
                            i.hostel = "J"
                            j_capacity = j_capacity-1
                        else:
                            i.hostel = "H"
                            h_capacity = h_capacity-1
                    else:
                        if h_capacity>0:
                            i.hostel = "H"
                            h_capacity = h_capacity-1
                        else:
                            i.hostel = "J"
                            j_capacity = j_capacity-1    
                else:
                    if i.preferenceOne=="PG":
                        if pg_capacity>0:
                            i.hostel = "PG"
                            pg_capacity = pg_capacity-1
                        else:
                            i.hostel = "I"
                            i_capacity = i_capacity-1
                    else:
                        if i_capacity>0:
                            i.hostel = "I"
                            i_capacity = i_capacity-1
                        else:
                            i.hostel = "PG"
                            pg_capacity = pg_capacity-1

class roomInformationView(APIView):
    def get(self, request, fromat=None):
        rooms = RoomInformationModel.objects.all()
        room_serializer = hostelRoomSerializer(rooms, many=True)
        return Response(room_serializer.data)

