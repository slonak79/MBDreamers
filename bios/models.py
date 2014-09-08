from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to="media")
    linkedin_link = models.URLField(max_length=250)
    personal_website_link = models.URLField(max_length=250, blank=True)
    bio = models.TextField()
    
