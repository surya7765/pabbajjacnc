from django.contrib import admin
from .models import Review, Product, ProductImage

# Register your models here.

admin.site.register(Review)
# admin.site.register(Product)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


class PropertyAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ]


admin.site.register(Product, PropertyAdmin)
