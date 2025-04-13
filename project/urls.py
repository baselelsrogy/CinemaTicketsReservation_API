from django.contrib import admin
from django.urls import path
from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 1
    path('django/jsonresponsemodel/', views.no_rest)
]
