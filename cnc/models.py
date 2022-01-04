from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from tinymce.models import HTMLField
from django.core.validators import RegexValidator
from PIL import Image
# Create your models here.
from io import BytesIO
from PIL import Image
from django.core.files import File


def compress(image):
    im = Image.open(image)
    # create a BytesIO object
    im_io = BytesIO()
    # save image to BytesIO object
    im.save(im_io, 'PNG', quality=95)
    # create a django-friendly Files object
    new_image = File(im_io, name=image.name)
    return new_image


class Review(models.Model):
    name = models.CharField(max_length=50, null=True)
    message = models.TextField(max_length=250,null=True)
    gmail = models.EmailField(max_length=50, null=True)
    published_date = models.DateTimeField(default=timezone.now, null=True)
    image = models.ImageField(
        upload_to='upload/', height_field=None, width_field=None, max_length=None, null=True)

    def save(self, *args, **kwargs):
        # call the compress function
        new_image = compress(self.image)
        # set self.image to new_image
        self.image = new_image
        # save
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(("Give your title"), max_length=50, null=True)
    price = models.CharField(("Enter Price"), max_length=10, null=True)
    availability = models.BooleanField(("Available or Not"))
    model_number = models.CharField(max_length=50, blank=True)
    video_url = models.URLField(max_length=300, null=True)
    image1 = models.ImageField(
        upload_to='upload/', max_length=None, blank=True, null=True)
    image2 = models.ImageField(
        upload_to='upload/', max_length=None, blank=True, null=True)
    image3 = models.ImageField(
        upload_to='upload/', max_length=None, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    automatic = models.BooleanField(
        ("Automatic or Manual"), default=False, null=True)
    weight = models.CharField(max_length=50, blank=True)
    plc_control = models.BooleanField(
        ("PLC Control"), default=False, null=True)
    computerized = models.BooleanField(
        ("Computerized or Manual"), default=False, null=True)
    supply_ability = models.BooleanField(
        ("Supply Ability"), default=False, null=True)

    detail = HTMLField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # call the compress function
        new_image1 = compress(self.image1)
        new_image2 = compress(self.image2)
        new_image3 = compress(self.image3)
        # set self.image to new_image
        self.image1 = new_image1
        self.image2 = new_image2
        self.image3 = new_image3
        # save
        super().save(*args, **kwargs)


class Book(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    date_book = models.DateTimeField(default=timezone.now, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    date_contact = models.DateTimeField(default=timezone.now, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.name
    

class Career(models.Model):
    designation = models.CharField(max_length=50, null=True)
    image_url = models.CharField(max_length=500, blank=True, null=True)
    job_location = models.CharField(max_length=50, null=True)
    job_description = HTMLField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now, null=True)
    responsibility = HTMLField(blank=True, null=True)
    skillset = HTMLField(blank=True, null=True)
    additional = HTMLField(blank=True, null=True)
    internship = models.BooleanField(("Internship"), default=False)

    def __str__(self):
        return self.designation


class CareerApplication(models.Model):
    name = models.CharField(max_length=50, null=True)
    gmail_id = models.EmailField(max_length=254, null=True)
    department = models.CharField(max_length=50, null=True)
    date_upload = models.DateTimeField(default=timezone.now, null=True)
    career = models.ForeignKey(Career, on_delete=models.CASCADE, null=True)
    contact_details = models.TextField(("Contact Details"), blank=True, null=True)
    resume = models.FileField(upload_to='upload/', blank=True, null=True)

    def __str__(self):
        return self.name
