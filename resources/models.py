from django.db import models
from bios.models import Author


class Resource(models.Model):
    date = models.DateTimeField()
    text = models.TextField()
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(Author)
    url_link = models.URLField()