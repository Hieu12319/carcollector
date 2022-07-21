from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car, Gas
from .forms import MaintenanceForm
# Create your views here.


def home(request):
    return HttpResponse('<h1> Hello Car-World </h1>')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', { 'cars' : cars })

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    gas_car_doesnt_have = Gas.objects.exclude(id__in = car.gases.all().values_list('id'))
    print(gas_car_doesnt_have)
    maintenance_form = MaintenanceForm()
    return render(request, 'cars/detail.html', {'car': car, 'maintenance_form': maintenance_form, 'gases' : gas_car_doesnt_have
    })
    

def add_maintenance(request, car_id):
    form = MaintenanceForm(request.POST)
    if form.is_valid():
        new_maintenance = form.save(commit=False)
        new_maintenance.car_id = car_id
        new_maintenance.save()
    return redirect('detail', car_id=car_id)

def assoc_gas(request, car_id, gas_id):
    Car.objects.get(id=car_id).gases.add(gas_id)
    return redirect('detail', car_id=car_id)

class CarCreate(CreateView):
    model = Car
    fields = ['make', 'model', 'year']
    success_url = '/cars/'

class CarUpdate(UpdateView):
    model = Car
    fields = ['make', 'model', 'year']

class CarDelete(DeleteView):
    model = Car
    success_url= '/cars/'

class GasList(ListView):
    model = Gas

class GasDetail(DetailView):
    model = Gas

class GasCreate(CreateView):
    model = Gas
    fields = '__all__'

class GasUpdate(UpdateView):
    model = Gas
    fields = ['name']

class GasDelete(DeleteView):
    model = Gas
    success_url = '/gas/'