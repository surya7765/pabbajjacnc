from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.


class Review(models.Model):
    username = models.CharField(max_length=50)
    message = models.CharField(max_length=250)
    published_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(
        upload_to='upload/', height_field=None, width_field=None, max_length=None)


class Product(models.Model):
    title = models.CharField(("Give your title"), max_length=50)
    manufacturing_date = models.DateField(
        ("Add Manufacturing date"), auto_now=False, auto_now_add=False)
    price = models.IntegerField(("Enter Price"))
    availability = models.BooleanField(("Available or Not"))
    item_number = models.CharField(max_length=50)
    model_numbeer = models.CharField(max_length=50)


class ProductImage(models.Model):
    title = models.ForeignKey(Product, default=None,
                              on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='upload/')
