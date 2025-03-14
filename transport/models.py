from django.db import models
from accounts.models import Profile

# Create your models here.
class Transport(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.TextField()
    time = models.DateTimeField()
    free_seats = models.IntegerField()
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    passengers = models.ManyToManyField(Profile, related_name='passengers', blank=True)

    @property
    def get_transport_through(self):
        return self.transportthroughlocation_set.all()
    
class TransportThroughLocation(models.Model):
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location
    

class TransportRequest(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.user.username + ' - ' + self.transport.user.user.username