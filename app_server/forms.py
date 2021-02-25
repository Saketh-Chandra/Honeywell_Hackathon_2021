from django import forms
from django.forms import ModelForm

from .models import *


class ObjectFormForms(forms.ModelForm):
    class Meta:
        model = Object
        fields = '__all__'


class ParamForm(forms.ModelForm):
    class Meta:
        model = Param
        fields = '__all__'
