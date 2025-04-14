from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest, Movie, Reservation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer, ReservationSerializer, GuestSerializer
from rest_framework import status, filters

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


# 2 model data default django without rest
def no_rest_from_model(request):
    
    data = Guest.objects.all()
    response = {
        'guests': list(data.values('name', 'mobile'))
    }
    
    return JsonResponse(response, safe=False)


# List == Get
# Create == Post
# Update == Put
# pk query == Get
# Delete == Delete


# 3 Function based-views
#3.1 GET POST
@api_view(['GET', 'POST'])
def FBV_List(request):
    # GET
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many= True)
        return Response(serializer.data)

    # POST
    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#3.2 GET PUT DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def FBV_pk(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        seriaizer = GuestSerializer(guest)
        return Response(seriaizer.data)
    # PUT
    elif request.method == 'PUT':
        seriaizer = GuestSerializer(guest, data=request.data)
        if seriaizer.is_valid():
            seriaizer.save()
            return Response(seriaizer.data, status=status.HTTP_200_OK)
        return Response(seriaizer.errors, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    elif request.method == 'PUT':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)