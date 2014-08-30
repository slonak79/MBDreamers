from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    dob = models.TextField()
    profile_photo = models.ImageField(upload_to="media")
    
