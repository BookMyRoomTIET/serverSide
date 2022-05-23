from django import forms
from .models import *


class hostelPreferenceFirstYearForm(forms.ModelForm):
    designation = forms.CharField(max_length=100)

    class Meta:
        model = hostelPreferenceFirstYear
        fields = ["name", "rollNumber", "cgpa", "preferenceOne","preferenceTwo"]

class hostelPreferenceSecondYearForm(forms.ModelForm):
    class Meta:
        model = hostelPreferenceSecondYear
        fields = ["name", "rollNumber", "cgpa", "preferenceOne","preferenceTwo"]