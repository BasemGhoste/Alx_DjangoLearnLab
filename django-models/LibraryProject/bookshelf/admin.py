from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')
    # Enable search functionality for these fields
    search_fields = ('title', 'author')
    # Add filters for these fields
    list_filter = ('publication_year',)
