from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Market, UserProfile
from .serializers import MarketSerializer, UserSerializer


class MarketAPIListCreate(generics.ListCreateAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    # permission_classes = (IsAuthenticated,)


class CatView(generics.ListAPIView):
    serializer_class = MarketSerializer

    def get_queryset(self):
        return Market.objects.filter(category_id=self.kwargs['category_id'])


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()