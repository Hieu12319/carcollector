from django.db import models
from django.urls import reverse

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.TextField()

    def __str__(self):
        return f"{self.make} - {self.model}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

MAINTAIN = (
    ('O', 'Oil Change'),
    ('T', 'Tire Rotation'),
    ('S', 'Spark plug'),
    ('V', 'Valve adjustement')
)
class Maintenance(models.Model):
    date = models.DateField('maintenance date')
    maintain = models.CharField(
        max_length=1,
        choices=MAINTAIN,
        default=MAINTAIN[0][0]
    )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_maintain_display()} on {self.date}"