from django.contrib import admin
from .models import Contacts
# Register your models here.

class ContactsAdmin(admin.ModelAdmin):
    list = ('name', 'number', 'relationship')

    admin.site.register(Contacts)