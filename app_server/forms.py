from django import forms
from django.forms import ModelForm

from .models import *


class ObjectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = ['Handle_1', 'Handle_2', 'Handle_3']


class ParamForm(forms.ModelForm):
    class Meta:
        model = Param
        fields = '__all__'
