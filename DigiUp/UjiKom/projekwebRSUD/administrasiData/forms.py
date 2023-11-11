from django import forms
from .models import DataPasien

class DataPasienForm(forms.ModelForm):
    class Meta:
        model = DataPasien
        fields = '__all__'
