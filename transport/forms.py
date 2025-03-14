from django.forms import ModelForm
from .models import Transport

class TransportForm(ModelForm):
    class Meta:
        model = Transport
        fields = ['description', 'time', 'free_seats', 'from_location', 'to_location']