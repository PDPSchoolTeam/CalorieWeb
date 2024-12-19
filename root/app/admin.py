from django.contrib import admin
from .models import FoodItem, Products, Product,About
from PIL import Image
import imagehash
# admin.site.register(Post)
admin.site.register(FoodItem)
admin.site.register(Product)
admin.site.register(About)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "product_type"]

    def save_model(self, request, obj, form, change):
        if obj.image:
            img = Image.open(obj.image)
            obj.image_hash = str(imagehash.average_hash(img))
        super().save_model(request, obj, form, change)

admin.site.register(Products, ProductAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

