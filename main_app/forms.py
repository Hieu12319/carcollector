from django.forms import ModelForm
from .models import Maintenance

class MaintenanceForm(ModelForm):
    class Meta:
        model = Maintenance
        fields= ['date', 'maintain']
        ordering = ['-date]']

    def __str__(self):
        return f"{self.get_maintain_display()} on {self.date}"

    