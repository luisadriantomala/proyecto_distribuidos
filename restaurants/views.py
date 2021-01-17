from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from restaurants.models import Restaurants
from restaurants.serializers import RestaurantsSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def restaurants_list(request):
    if request.method == 'GET':
        restaurants = Restaurants.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            restaurants = restaurants.filter(title__icontains=title)
        
        restaurants_serializer = RestaurantsSerializer(restaurants, many=True)
        return JsonResponse(restaurants_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        restaurants_data = JSONParser().parse(request)
        restaurants_serializer = RestaurantsSerializer(data=restaurants_data)
        if restaurants_serializer.is_valid():
            restaurants_serializer.save()
            return JsonResponse(restaurants_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(restaurants_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

    