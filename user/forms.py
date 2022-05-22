from django import forms
from rest_framework.authtoken.models import Token
from user.models import *
from django.db import transaction


class WardenCreationForm(forms.ModelForm):
    designation = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ("email", "phone", "name", "password","registration_id")

    @transaction.atomic
    def save(self, commit=True):
        user = super(WardenCreationForm, self).save(commit=False)
        user.is_warden = True
        user.set_password(self.cleaned_data["password"])
        user.name = user.name.capitalize()
        user.save()
        Token.objects.create(user=user)
        warden = Warden(user=user, designation=self.cleaned_data["designation"].capitalize())
        warden.save()
        return user


class StudentCreationForm(forms.ModelForm):
    grad_year = models.IntegerField()
    branch = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    class Meta:
        model = User
        fields = ("email", "phone", "name", "password","registration_id")

    @transaction.atomic
    def save(self, commit=True):
        user = super(StudentCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.name = user.name.capitalize()
        user.save()
        Token.objects.create(user=user)
        student = Student(user=user,sex=self.cleaned_data.get('sex'),branch=self.cleaned_data.get('branch'),grad_year=self.cleaned_data.get('grad_year'))
        student.save()
        return user