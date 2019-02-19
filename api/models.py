from django.db import models
from rest_framework import routers, serializers, viewsets
from restaurants.models import Restaurant
# Create your models here.
class RestaurantListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = '__all__'
