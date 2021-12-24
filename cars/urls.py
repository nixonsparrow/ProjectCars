from django.urls import path
from cars import views

urlpatterns = [
    path('cars/', views.car_list, name='car-list'),
]
