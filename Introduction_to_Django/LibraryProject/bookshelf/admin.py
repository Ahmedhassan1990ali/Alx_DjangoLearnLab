from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Enable filters for these fields
    list_filter = ('author', 'publication_year')

    # Enable search functionality for these fields
    search_fields = ('title', 'author')


# Register your models here.
admin.site.register(Book, BookAdmin)