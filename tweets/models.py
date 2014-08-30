from django.db import models

class Tweet(models.Model):
    date = models.DateField()
    latitude = models.DecimalField(max_digits=6 , decimal_places=6)
    longitude = models.DecimalField(max_digits=6 ,decimal_places=6)
    sentiment = models.BooleanField()
    content = models.TextField()
    tweetID = models.CharField(max_length=200)
