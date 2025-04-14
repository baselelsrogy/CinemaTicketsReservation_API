from django.contrib import admin
from django.urls import path
from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 1
    path('django/jsonresponsemodel/', views.no_rest),
    #2
    path('django/jsonfrommodels/', views.no_rest_from_model),
    #3.1 GET POST from rest framework function based-views @api_view
    path('rest-fbv/', views.FBV_List),
    #3.2 GET PUT DELETE from rest framework function based-views @api_view
    path('rest-fbv/<int:pk>/', views.FBV_pk)
]
