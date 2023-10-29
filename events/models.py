from django.db import models
from users.models import Profile


class Event(models.Model):
    name = models.CharField(max_length=128)
    creator = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)  # should be linked to CapX user ID and not the profile ID
    date_of_creation = models.DateField()
    date_of_last_edit = models.DateField()
    description = models.CharField(max_length=512)
    wiki_link = models.URLField(max_length=256)
    in_person_event = models.BooleanField()
    country = models.CharField(max_length=50)