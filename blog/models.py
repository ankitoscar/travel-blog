from django.db import models
from django_countries.fields import CountryField
import uuid

# Create your models here.
class Blogger(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    country = CountryField()
    about = models.CharField(max_length=140, blank='Write something about yourself in 140 characters.')