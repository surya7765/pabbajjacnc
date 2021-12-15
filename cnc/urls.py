from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('', views.home, name="home"),
    path('faq/', views.faq, name="faq"),
    path('career/', views.career, name="career"),
    path('about/', views.about, name="about"),
    path('product/', ProductListView.as_view(), name="product"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product-detail"),
]
