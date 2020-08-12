from django.shortcuts import render
from rest_framework import viewsets
from .models import Client
from .serializer import ClientSerializer
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
# from rest_framework.permissions import IsAuthenticated


class ClientViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
