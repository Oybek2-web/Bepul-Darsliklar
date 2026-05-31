from django.shortcuts import render, redirect, get_object_or_404
from .models import Darslik
from .forms import DarslikForms

def darslik_create(request):
    if request.method == 'POST':
        form = DarslikForms(request.POST, request.FILES)

        if form.is_valid():
            new_darslik = form.save()

            return redirect(
                'fanlar:darslik_kirish',
                id=new_darslik.fan_nomi.id
            )
    else:
        form = DarslikForms()

    return render(request, 'darslik/darslik_create.html', {'form': form})

def darslik_update(request, id):
    darslik = get_object_or_404(Darslik, id=id)

    if request.method == 'POST':
        form = DarslikForms(request.POST, request.FILES, instance=darslik)

        if form.is_valid():
            updated_darslik = form.save()

            return redirect(
                'fanlar:darslik_kirish',
                id=updated_darslik.fan_nomi.id
            )

    else:
        form = DarslikForms(instance=darslik)

    return render(request, 'darslik/darslik_update.html', {
        'form': form,
        'darslik': darslik
    })

def darslik_delete(request, id):
    fan = get_object_or_404(Darslik, id=id)
    fan_id = fan.fan_nomi.id
    fan.delete()
    return redirect('fanlar:darslik_kirish', id=fan_id)


def darslik_detail(request, id):
    darslik = get_object_or_404(Darslik, id=id)
    return render(request, 'darslik/darslik_detail.html', {'darslik':darslik})

