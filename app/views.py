from django.shortcuts import render
from rest_framework import generics
from .models import User, Work, Artist, Client
from .serializers import UserSerializer, WorkSerializer, ArtistSerializer
from rest_framework.permissions import AllowAny
from .filter import WorkFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class WorkApiView(generics.ListAPIView):
    serializer_class = WorkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = WorkFilter

    def get_queryset(self):
        queryset_work = Work.objects.all()
        queryset_art = Artist.objects.all()
        if queryset_work:
            filtered_queryset = self.filter_queryset(queryset_work)
            return filtered_queryset
        filtered_queryset = self.filter_queryset(queryset_art)
        return filtered_queryset
        