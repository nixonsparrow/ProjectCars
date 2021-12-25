from django.urls import path
from cars import views

urlpatterns = [
    path('cars/', views.car_list, name='car-list'),
    path('cars/<int:pk>/', views.car_detail, name='car-detail'),
    path('rate/', views.add_rate, name='add-rate'),
]
