from django.contrib import admin
from .models import Car, Maintenance, Gas, Photo    

# Register your models here.
admin.site.register(Car)
admin.site.register(Maintenance)
admin.site.register(Gas) 
admin.site.register(Photo)