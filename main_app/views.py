from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
class Car:  
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
   

cars = [
  Car('Honda', 'Civic', '1996'),
  Car('Chevy', 'Corvette', '2012'),
  Car('Dodge', 'Viper', '2002'),
]

def home(request):
    return HttpResponse('<h1> Hello Car-World </h1>')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    return render(request, 'cars/index.html', { 'cars' : cars })