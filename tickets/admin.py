from django.contrib import admin
from .models import Guest, Movie, Reservation

# Register your models here.
admin.site.register(Guest)
admin.site.register(Movie)
admin.site.register(Reservation)
