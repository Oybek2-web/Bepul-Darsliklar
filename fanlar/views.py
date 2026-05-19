from django.shortcuts import render, redirect, get_object_or_404

from account.utils import login_required
from .models import Fanlar
from .forms import FanlarForms
# FANLAR MODELI

def fanlar_list(request):
    fanlar = Fanlar.objects.all()
    return render(request, 'fanlar/fanlar_list.html', {"fanlar":fanlar})

@login_required
def fanlar_create(request):
    if request.method == 'POST':
        form = FanlarForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fanlar:fanlar_list')
    else:
        form = FanlarForms()
    return render(request, 'fanlar/fanlar_create.html', {"form": form})

@login_required
def fanlar_update(request, id):
    fanlar = get_object_or_404(Fanlar, id=id)
    if request.method == "POST":
        form = FanlarForms(request.POST, instance=fanlar)
        if form.is_valid():
            form.save()
            return redirect('fanlar:fanlar_list')
    else:
        form = FanlarForms(instance=fanlar)
    return render(request, 'fanlar/fanlar_update.html', {"form":form})

def fanlar_delete(request, id):
    fanlar = get_object_or_404(Fanlar, id=id)
    fanlar.delete()
    return redirect('fanlar:fanlar_list')

def darslik_kirish(request, id):
    kirish = get_object_or_404(Fanlar, id=id)
    darsliklar = kirish.darsliklar.all()
    return render(request,'fanlar/darslik_kirish.html',{'kirish': kirish, 'darsliklar': darsliklar})