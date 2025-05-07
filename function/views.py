from django.shortcuts import render
from rest_framework import viewsets
from .models import MenuItem, Contact
from .serializers import MenuItemSerializer, ContactSerializer

# Create your views here.


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

