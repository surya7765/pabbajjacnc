from django.contrib import admin
from .models import Review, Product, Career, Contact

# Register your models here.

admin.site.register(Review)
admin.site.register(Product)
admin.site.register(Career)
admin.site.register(Contact)
