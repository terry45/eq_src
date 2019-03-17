from django.shortcuts import render

from .forms import EquipmentForm


def add(request):
    form = EquipmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EquipmentForm()
    context = {
        'form': form
    }
    return render(request, 'register/add.html', context)


def delete(request):
    return render(request, 'register/delete.html')


def list(request):
    return render(request, 'register/list.html')


def search(request):
    return render(request, 'register/search.html')
