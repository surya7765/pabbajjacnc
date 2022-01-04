from django.contrib import admin
from .models import Review, Product,Book, Career, Contact, CareerApplication

# Register your models here.

admin.site.register(Review)
admin.site.register(Product)
admin.site.register(Career)
admin.site.register(Contact)
admin.site.register(CareerApplication)
admin.site.register(Book)
