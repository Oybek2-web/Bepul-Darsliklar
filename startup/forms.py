from django.forms import forms
from .models import StartUp

class StartUpForm(forms.Form):
    class Meta:
        model = StartUp
        fields = '__all__'