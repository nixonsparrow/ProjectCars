from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import renderer_classes, api_view
from rest_framework import status
from django.shortcuts import render
from .models import Car
from .serializers import CarSerializer, RateSerializer, PopularCarSerializer


def welcome(request):
    return render(request, 'cars/welcome.html')


@api_view(('GET', 'POST'))
@renderer_classes((JSONRenderer,))
def car_list(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def car_popular(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = PopularCarSerializer(cars, many=True)
        return Response(serializer.data)


@api_view(('DELETE',))
@renderer_classes((JSONRenderer,))
def car_detail(request, pk):
    try:
        car = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(('POST', ))
@renderer_classes((JSONRenderer,))
def add_rate(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        translated_data = {'car': data['car_id'], 'rate': data['rating']}
        serializer = RateSerializer(data=translated_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
