from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Car(models.Model):
    make = models.CharField(max_length=50, default='', null=False, blank=False)
    model = models.CharField(max_length=50, default='', null=False, blank=False)

    def avg_rating(self):
        if not len(self.rates.all()): return None
        return float(format(self.rates.aggregate(models.Sum('rate'))['rate__sum'] / len(self.rates.all()), '.1f'))

    def rates_number(self):
        return self.rates.aggregate(models.Count('rate'))['rate__count']

    def rate_me(self, rate):
        return Rate.objects.create(car=self, rate=rate)

    def __str__(self):
        return f'{self.make} {self.model}'


class Rate(models.Model):
    RATES = (
        (1, 'Meh'),
        (2, 'Nothing special'),
        (3, 'Pretty OK'),
        (4, 'Likeable'),
        (5, 'Extraordinary!'),
    )
    rate = models.IntegerField(choices=RATES, validators=[MaxValueValidator(5), MinValueValidator(1)])
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='rates')
