from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1> Hello Car-World </h1>')

def about(request):
    return HttpResponse('This is my Car collector About page')