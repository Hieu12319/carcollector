from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car
# Create your views here.
#class Car:  
#  def __init__(self, make, model, year):
#    self.make = make
##    self.year = year
   

# Car('Honda', 'Civic', '1996'),
#  Car('Chevy', 'Corvette', '2012'),
#  Car('Dodge', 'Viper', '2002'),
#]

def home(request):
    return HttpResponse('<h1> Hello Car-World </h1>')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', { 'cars' : cars })

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/detail.html', {'car': car})

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