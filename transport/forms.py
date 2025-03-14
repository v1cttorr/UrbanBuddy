from django.forms import ModelForm
from .models import Transport, Alert

class TransportForm(ModelForm):
    class Meta:
        model = Transport
        fields = ['description', 'time', 'free_seats', 'from_location', 'to_location']

class AlertForm(ModelForm):
    class Meta:
        model = Alert
        fields = ['name', 'time', 'address']