from django.shortcuts import render

from .forms import DeviceForm
from django.views.generic import ListView
from .models import Device

def add(request):
    form = DeviceForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = DeviceForm()
    context = {
        'form': form
    }
    return render(request, 'register/add.html', context)


def delete(request):
    return render(request, 'register/delete.html')


class DeviceListView(ListView):
    model = Device
    template_name = 'register/list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'device'
    ordering = ['ins_ref']

