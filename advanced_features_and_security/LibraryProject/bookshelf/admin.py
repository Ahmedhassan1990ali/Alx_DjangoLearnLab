from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book ,CustomUser


class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Enable filters for these fields
    list_filter = ('author', 'publication_year')

    # Enable search functionality for these fields
    search_fields = ('title', 'author')

class CustomUserAdmin(UserAdmin):
    pass

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)