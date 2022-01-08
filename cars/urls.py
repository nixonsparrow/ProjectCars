from django.urls import path
from cars import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('cars/', views.CarListAPI.as_view(), name='car-list'),
    path('cars/<int:pk>/', views.car_detail, name='car-detail'),
    path('rate/', views.AddRateAPI.as_view(), name='add-rate'),
    path('popular/', views.CarPopularAPI.as_view(), name='car-popular'),
]
