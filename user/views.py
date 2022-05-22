from re import search
import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from .serializers import *
from .forms import *
from .models import *
from django.db.models import Q
import os
from .custompermissions import *


class WardenRegisterView(APIView):
    def post(self, request):
        form = WardenCreationForm(request.data)
        if form.is_valid():
            form.save()
            return Response({"detail": "Warden registered successfully"})
        else:
            return Response(
                {"detail": "Warden registration failed", "errors": form.errors}, status=400)

class WardenView(APIView):
    def get(self, request):
        warden = Warden.objects.all()
        serializer = WardenSerializer(warden, many=True)
        return Response(serializer.data)

class StudentRegisterView(APIView):
    def post(self, request):
        form = StudentCreationForm(request.data)
        if form.is_valid():
            form.save()
            return Response({"detail": "Student registered successfully"})
        else:
            return Response(
                {"detail": "Student registration failed", "errors": form.errors}, status=400)

class currentUserInfoView(APIView):
    permission_classes = (IsAuthenticated,isStudent)
    def get(self, request):
        user = request.user.name
        sex = request.user.student.sex
        grad_year = request.user.student.grad_year
        info = {"name": user,"sex":sex,"grad_year":grad_year}
        return Response(info)