from django.db import models

class location(models.Model):
    id = models.IntegerField(
        primary_key=True,
        null=False,
        auto_created=True,
    )
    location_name = models.CharField(
        max_length=50,
        null=False
    )

class object_type(models.Model):
    location_name = models.CharField(
        max_length=50,
        null=False
    )

class Ticket(models.Model):
   
    def __str__(self):
        return True