from django.db import models
from django.utils import timezone

# Create your models here.


class Review(models.Model):
    username = models.CharField(max_length=50)
    message = models.CharField(max_length=250)
    published_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(
        upload_to='upload/', height_field=None, width_field=None, max_length=None)
