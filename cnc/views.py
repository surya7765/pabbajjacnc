from django.shortcuts import render
from .models import Review
# Create your views here.


def home(request):

    review = Review.objects.all()

    context = {
        'review': review
    }

    return render(request, 'index.html', context)


def faq(request):
    return render(request, 'faq.html')
