from django.shortcuts import render
from .models import Review
from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView


def home(request):

    review = Review.objects.all()
    products = Product.objects.all()[:3]
    context = {
        'review': review,
        'products': products
    }
    return render(request, 'index.html', context)


def faq(request):
    return render(request, 'faq.html')


def about(request):
    return render(request, 'about.html')

def career(request):
    context = {'careers': Career.objects.all()}
    return render(request, 'career.html', context)


class CareerListView(ListView):
    model = Career
    template_name = 'career.html'
    context_object_name = 'careers'
    paginate_by = 9


def product(request):
    context = {'products': Product.objects.all()}
    return render(request, 'product.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'products'
    paginate_by = 9


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
