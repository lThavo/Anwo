from django import forms
from django.forms import ModelForm, fields
from .models import Aire
 
class AireForm(ModelForm):
    class Meta:
        model = Aire
        fields = ['codigo', 'tipo', 'btu', 'imagen', 'categoria']