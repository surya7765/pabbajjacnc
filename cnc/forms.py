from django.forms import ModelForm
from .models import Review, Book, Contact, CareerApplication, Product
from django import forms


class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ('name', 'gmail', 'image', 'message')


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'email','phone_number', 'message')

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'phone_number', 'message')

class CareerApplicationForm(ModelForm):
    class Meta:
        model = CareerApplication
        fields = ('name', 'gmail_id', 'department',
                  'contact_details', 'resume')
