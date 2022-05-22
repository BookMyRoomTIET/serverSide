from django.urls import path,include
from .views import *

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path("register/warden/", WardenRegisterView.as_view(), name="warden_register"),
    path("register/student/", StudentRegisterView.as_view(), name="student_register"),
    path("warden/", WardenView.as_view(), name="warden_view"),
    path("student/", currentUserInfoView.as_view(), name="student_view"),
]
