from django.contrib import admin
from .models import Transport, TransportThroughLocation, TransportRequest

# Register your models here.
admin.site.register(Transport)
admin.site.register(TransportThroughLocation)
admin.site.register(TransportRequest)