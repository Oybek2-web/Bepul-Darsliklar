from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from account.forms import RegisterForm

from django.contrib.auth.models import User

# REGISTER
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data.get('username'),
                password=data.get('password')
            )
            login(request, user)
            return redirect('fanlar:fanlar_list')
        else:
            return render(request, 'account/register.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'account/register.html', {'form': form})


# LOGIN
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next') or request.POST.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('fanlar:fanlar_list')
    else:
        form = AuthenticationForm()
    return render(request,'account/login.html',{'form': form})


def logout_user(request):
    logout(request)
    return redirect('account:login')
