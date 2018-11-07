from django.contrib import admin

# Register your models here.

from .models import Book, Topic

admin.site.register(Book)
admin.site.register(Topic)
