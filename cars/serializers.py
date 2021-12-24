from rest_framework import serializers
from .models import Car, Rate


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


# class CarSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     make = serializers.CharField(required=True, allow_blank=False, max_length=50)
#     model = serializers.CharField(required=True, allow_blank=False, max_length=50)
#
#     def create(self, validated_data):
#         return Car.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.make = validated_data.get('make', instance.make)
#         instance.model = validated_data.get('model', instance.model)
#         instance.save()
#         return instance
