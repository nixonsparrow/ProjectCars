from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Rate


@receiver(post_save, sender=Rate)
def create_profile(sender, instance, created, **kwargs):
    if created:
        car = instance.car
        car.avg_rating = car.calculate_avg_rating()
        car.save()
