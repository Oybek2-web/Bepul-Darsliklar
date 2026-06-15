from django.shortcuts import render, redirect, get_object_or_404
from .models import StartUp
from .forms import StartUpForm
from django.contrib.auth.decorators import login_required

@login_required
def startup_list(request):
    startup = StartUp.objects.all()
    return render(request, 'startup/startup_list.html', {'startup':startup})

def startup_create(request):
    if request.method == 'POST':
        form = StartUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('startup_list')
        return render(request, 'startup/startup_create.html', {'form':form})
    form = StartUpForm()
    return render(request, 'startup/startup_create.html', {'form':form})

def startup_update(request, id):
    startup = get_object_or_404(StartUp, id=id)
    if request.method == 'POST':
        form = StartUpForm(request.POST, request.FILES, instance=startup)
        if form.is_valid():
            form.save()
            return redirect('startup_list')
        return render(request, 'startup/startup_update.html', {'form': form})
    form = StartUpForm(instance=startup)
    return render(request, 'startup/startup_update.html', {'form':form})

def startup_delete(request, id):
    startup = get_object_or_404(StartUp, id=id)
    startup.delete()
    return redirect('startup_list')

def startup_detail(request, id):
    startup = get_object_or_404(StartUp, id=id)
    return render(request, 'startup/startup_detail.html', {'startup':startup})


