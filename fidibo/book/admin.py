from django.contrib import admin
from .models import Book



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "digital_version")
    search_fields = ("title", "author__full_name")
    prepopulated_fields = {"slug": ("title",)}

