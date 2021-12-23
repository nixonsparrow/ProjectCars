from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=50, default='', null=False, blank=False)
