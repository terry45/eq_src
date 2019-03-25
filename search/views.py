from django.shortcuts import render
from register.models import Device
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def search_form(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            device = Device.objects.all()
            return render(request, 'search/search_results.html', {'device': device, 'query': q})
    return render(request, 'search/search_form.html', {'error': error})


