from django.shortcuts import render, redirect, get_object_or_404
from .models import Darslik
from .forms import DarslikForms

def darslik_create(request):
    if request.method == 'POST':
        form = DarslikForms(request.POST, request.FILES)
        if form.is_valid():
            darslik = form.save()
            return redirect('fanlar:darslik_kirish', darslik.fan.id)
    else:
        form = DarslikForms()
    return render(request, 'darslik/darslik_create.html', {'form': form})

def darslik_update(request, id):
    darslik = get_object_or_404(Darslik, id=id)
    if request.method == "POST":
        form = DarslikForms(request.POST, request.FILES, instance=darslik)
        if form.is_valid():
            form.save()
            return redirect('fanlar:darslik_kirish')
    else:
        form = DarslikForms(instance=darslik)
    return render(request, 'darslik/darslik_update.html', {"form":form})

def darslik_delete(request, id):
    fan = get_object_or_404(Darslik, id=id)
    fan.delete()
    return redirect('fanlar:darslik_kirish')
