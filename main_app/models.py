from django.db import models
from django.urls import reverse

MAINTAIN = (
    ('O', 'Oil Change'),
    ('T', 'Tire Rotation'),
    ('S', 'Spark plug'),
    ('V', 'Valve adjustement')
)
# Create your models here.
class Gas(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('gas_detail', kwargs={'pk': self.id})


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.TextField()

    def __str__(self):
        return f"{self.make} - {self.model}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})


class Maintenance(models.Model):
    date = models.DateField('Maintenance Date')
    maintain = models.CharField(
        max_length=1,
        choices=MAINTAIN,
        default=MAINTAIN[0][0]
    )

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_maintain_display()} on {self.date}"
    
    