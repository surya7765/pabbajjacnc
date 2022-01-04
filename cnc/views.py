from django.shortcuts import render
from .models import Review
from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView
from django.template.loader import get_template
from xhtml2pdf import pisa
from .forms import ReviewForm, ContactForm, BookForm, CareerApplicationForm
from django.urls import reverse, reverse_lazy


def home(request):

    reviews = Review.objects.all().order_by('-id')[:3]
    products = Product.objects.all()[:3]
    context = {
        'reviews': reviews,
        'products': products,
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


class CareerDetailView(DetailView):
    model = Career
    template_name = "career_detail.html"


def product(request):
    context = {'products': Product.objects.all()}

    return render(request, 'product.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'products'
    ordering = ['-date_posted']
    paginate_by = 9


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


def post_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    product = get_object_or_404(Product, pk=pk)
    template_path = 'pdf_view.html'
    context = {'product': product}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="{product.title}.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def review(request):
    data = {}
    form = ReviewForm(request.POST, request.FILES)
    if request.is_ajax():
        if form.is_valid():
            form.save()
            data['name'] = form.cleaned_data.get('name')
            data['status'] = 'ok'
            return JsonResponse(data)

    context = {'review_form': form}

    return render(request, 'review_form.html', context)


def contact(request):
    data = {}
    form = ContactForm()
    if request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            data['name'] = form.cleaned_data.get('name')
            data['status'] = 200
            return JsonResponse(data)

    context = {'contact_form': form}

    return render(request, 'contact.html', context)


class CareerApplyView(CreateView):
    model = CareerApplication
    form_class = CareerApplicationForm
    template_name = 'career_apply.html'
    success_url = reverse_lazy('career')

    def form_valid(self, form):
        form.instance.career_id = self.kwargs['pk']
        return super().form_valid(form)


class ContactView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'product_book.html'
    success_url = reverse_lazy('product')

    def form_valid(self, form):
        form.instance.product_id = self.kwargs['pk']
        return super().form_valid(form)
