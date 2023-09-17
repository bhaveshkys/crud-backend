from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=250)
    number = models.IntegerField()
    relationship = models.CharField(max_length=350)

    def __str__(self):
        return self.name