from django.contrib import admin
from .models import Transport, TransportThroughLocation, Alert

# Register your models here.
admin.site.register(Transport)
admin.site.register(TransportThroughLocation)
admin.site.register(Alert)