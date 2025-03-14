from django.db import models

# Create your models here.


class Event(models.Model):
    category_choices = (
        ('Music', 'Music'),
        ('Sport', 'Sport'),
        ('Art', 'Art'),
        ('Theatre', 'Theatre'),
        ('Comedy', 'Comedy'),
        ('Festival', 'Festival'),
        ('Exhibition', 'Exhibition'),
        ('Conference', 'Conference'),
        ('Party', 'Party'),
        ('Other', 'Other'),
    )

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(choices=category_choices, max_length=100, default='Other')
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/images/', null=True, blank=True)

    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url