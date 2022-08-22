from django import forms
from django.forms import TextInput

from home.models import ExeltoData, AllData


class UpdateForm(forms.ModelForm):
    class Meta:
        model = ExeltoData
        fields = '__all__'


class SendDataForm(forms.ModelForm):
    class Meta:
        model = AllData
        fields = '__all__'
