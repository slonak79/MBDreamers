from django.db import models

class Event(models.Model):
    event_name = models.DateField()
    Address = models.CharField(max_length = 200)
    date = models.DateTimeField()
    description = models.TextField()
