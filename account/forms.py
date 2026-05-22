from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Ikkita parol bir xil emas!')
        return self.cleaned_data

# class LoginForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput)
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     def clean(self):
#         data = self.cleaned_data
#         user = authenticate(username=data.get('username'), password=data.get('password'))
#
#         if not user:
#             raise forms.ValidationError('Username yoki Parol xato!')
#
#         return {'user': user}

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Username yoki Parol xato!')

            cleaned_data['user'] = user
        return cleaned_data