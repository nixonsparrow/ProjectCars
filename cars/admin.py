from django.contrib import admin
from cars.models import Car, Rate


class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'make', 'model', 'avg_rating', 'rates_number']


class RateAdmin(admin.ModelAdmin):
    list_display = ['id', 'car', 'rate']


admin.site.register(Car, CarAdmin)
admin.site.register(Rate, RateAdmin)
