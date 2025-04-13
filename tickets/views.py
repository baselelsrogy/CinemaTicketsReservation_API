from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.

# 1 without REST
def no_rest(request):
    guests = [
        {
            'id':1,
            'name':'Basel',
            'mobile':21159768824
        },
        {
            'id':2,
            'name':'Hamza',
            'mobile':21159768834
        },
    ]
    
    return JsonResponse(guests, safe=False)
