from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.


from rest_framework import generics, status

from .models import Market
from .serializers import MarketSerializer
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

class MarketAPIListCreate(generics.ListCreateAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    #permission_classes = (IsAuthenticated,)




class CatView(generics.ListAPIView):
    serializer_class = MarketSerializer

    def get_queryset(self):
        return Market.objects.filter(category_id=self.kwargs['category_id'])


# class UserView(generics.ListCreateAPIView):
#     serializer_class = UserSerializer
#     queryset = UserProfile.objects.all()