from django.shortcuts import render
from .models import Contacts
from .serializers import ContactsSerializer
from rest_framework import viewsets

# Create your views here.
class ContactsViewSet(viewsets.ModelViewSet):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()