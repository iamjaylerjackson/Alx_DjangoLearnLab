from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters for easy data filtering
    list_filter = ('author', 'publication_year')

    # Enable search functionality
    search_fields = ('title', 'author')
