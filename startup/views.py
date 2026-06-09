from django.shortcuts import render, redirect
from .models import StartUp
from .forms import StartUpForm


def startup_list(request):
    startup = StartUp.objects.all()
    return render(request, 'startup/startup_list.html', {'startup':startup})

def startup_create(request):
    if request.method == 'POST':
        form = StartUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('startup:list')
        return render(request, 'startup/startup_create.html', {'form':form})
    form = StartUpForm()
    return render(request, 'startup/startup_create.html', {'form':form})

# Create your views here.
