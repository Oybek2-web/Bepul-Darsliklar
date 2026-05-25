from django import forms
from .models import Darslik

class DarslikForms(forms.ModelForm):
    class Meta:
        model = Darslik
        fields = ['photo', 'video', 'pdf', 'title', 'describe']