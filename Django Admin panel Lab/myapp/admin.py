from django.contrib import admin 
from .models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'genre', 'is_available')
    list_filter = ('genre', 'is_available', 'published_date')
    search_fields = ('title', 'author')
    list_editable = ('is_available',)
    ordering = ('-published_date',)
    date_hierarchy = 'published_date'
    fields = ('title', 'author', 'genre', 'published_date', 'is_available')
    list_per_page = 10

admin.site.register(Book, BookAdmin)