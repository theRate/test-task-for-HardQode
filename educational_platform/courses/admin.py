from django.contrib import admin

from .models import Product, Lesson, Group

# Register your models here.
admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(Group)