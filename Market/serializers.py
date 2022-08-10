
from rest_framework import serializers

from .models import Market,UserProfile


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ("__all__")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("__all__")