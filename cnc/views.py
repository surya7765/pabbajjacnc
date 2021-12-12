from django.shortcuts import render
from .models import Review
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImage
# Create your views here.


def home(request):

    review = Review.objects.all()

    context = {
        'review': review
    }

    return render(request, 'index.html', context)


def faq(request):
    return render(request, 'faq.html')


def product_view(request):
    product = Product.objects.all()
    photos = ProductImage.objects.filter(title=product.title)
    print(photos)
    return render(request, 'index.html', {
        'product': product,
        'photos': photos
    })
