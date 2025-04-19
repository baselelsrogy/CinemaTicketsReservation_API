from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Guest -- Movie -- Reservation

class Guest(models.Model):
    
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=12)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    
    hall = models.CharField(max_length=30)
    movie = models.CharField(max_length=50)
    date = models.DateField()
    
    def __str__(self):
        return self.movie    

class Reservation(models.Model):
    
    guest = models.ForeignKey(Guest, related_name='reservation', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reservation', on_delete=models.CASCADE)
    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()


# create automatic token when new user was register    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)