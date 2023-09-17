from rest_framework import serializers
from backend_api.models import Contacts

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'