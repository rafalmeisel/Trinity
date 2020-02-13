from django.contrib import admin

# Register your models here.
from library.api.models import Book

admin.site.register(Book)