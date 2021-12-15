from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from tinymce.models import HTMLField
from django.core.validators import RegexValidator

# Create your models here.


class Review(models.Model):
    username = models.CharField(max_length=50)
    message = models.CharField(max_length=250)
    published_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(
        upload_to='upload/', height_field=None, width_field=None, max_length=None)


class Product(models.Model):
    title = models.CharField(("Give your title"), max_length=50)
    price = models.CharField(("Enter Price"), max_length=10)
    availability = models.BooleanField(("Available or Not"))
    model_number = models.CharField(max_length=50, blank=True)
    image1 = models.ImageField(
        upload_to='upload/', max_length=None, blank=True, null=True)
    image2 = models.ImageField(
        upload_to='upload/', max_length=None, blank=True, null=True)
    image3 = models.ImageField(
        upload_to='upload/', max_length=None, blank=True, null=True)

    automatic = models.BooleanField(("Automatic or Manual"), default=False)
    weight = models.CharField(max_length=50, blank=True)
    plc_control = models.BooleanField(("PLC Control"), default=False)
    computerized = models.BooleanField(
        ("Computerized or Manual"), default=False)
    supply_ability = models.BooleanField(("Supply Ability"), default=False)

    detail = HTMLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{10,13}$', message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=15, blank=True)
    published_date = models.DateTimeField(default=timezone.now)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Career(models.Model):
    designation = models.CharField(max_length=50)
    image_url = models.CharField(max_length=500, blank=True)
    job_location = models.CharField(max_length=50)
    job_description = HTMLField(blank=True, null=True)
    responsibility = HTMLField(blank=True, null=True)
    skillset = HTMLField(blank=True, null=True)
    additional = HTMLField(blank=True, null=True)
    internship = models.BooleanField(("Internship"), default=False)
