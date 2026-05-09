from django import forms
from .models import Darslik

class DarslikForms(forms.ModelForm):
    class Meta:
        model = Darslik
        fields = '__all__'