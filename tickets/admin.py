from django.contrib import admin
from .models import Guest, Movie, Reservation, Post

# Register your models here.
admin.site.register(Guest)
admin.site.register(Post)
admin.site.register(Movie)
admin.site.register(Reservation)
