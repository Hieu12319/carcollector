from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Car, Gas, Photo
from .forms import MaintenanceForm
import uuid
import boto3

# Create your views here.

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'carcollecto'


def home(request):
    return HttpResponse('<h1> Hello Car-World </h1>')

def about(request):
    return render(request, 'about.html')

@login_required
def cars_index(request):
    cars = Car.objects.filter(user=request.user)
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

def add_photo(request, car_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, car_id=car_id)
            photo.save()
        except:
            print('An error occured uploading file to s3')
    return redirect('detail', car_id=car_id)
    
class CarCreate(CreateView):
    model = Car
    fields = ['make', 'model', 'year']
    success_url = '/cars/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)