from django.urls import path
from . import views
from .views import ContactView, ProductListView, ProductDetailView, CareerDetailView, CareerApplyView

urlpatterns = [
    path('', views.home, name="home"),
    path('faq/', views.faq, name="faq"),
    path('career/', views.career, name="career"),
    path('about/', views.about, name="about"),
    path('product/', ProductListView.as_view(), name="product"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product-detail"),
    path('product/<int:pk>/book/', ContactView.as_view(), name="product-book"),
    path('review/', views.review, name="review"),
    path('contact/', views.contact, name="contact"),
    path('career/<int:pk>/', CareerDetailView.as_view(), name="career-detail"),
    path('career/<int:pk>/apply/', CareerApplyView.as_view(), name="career-apply"),
    path('product/<int:pk>/pdf/', views.post_render_pdf_view, name="product-pdf"),
]
