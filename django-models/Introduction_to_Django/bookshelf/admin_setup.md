# Django Admin Configuration for Book Model

## Steps Performed

1. Registered the `Book` model in `bookshelf/admin.py`.
2. Customized the admin display using the `BookAdmin` class.

## Code Implementation

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
```
