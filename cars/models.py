from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Car(models.Model):
    make = models.CharField(max_length=50, default='', null=False, blank=False)
    model = models.CharField(max_length=50, default='', null=False, blank=False)

    def __str__(self):
        return f'{self.make} | {self.model}'


class Rate(models.Model):
    rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='rates')
