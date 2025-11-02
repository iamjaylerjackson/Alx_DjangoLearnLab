# Delete Operation

This command deletes the Book record and confirms it has been removed from the database.

```python
from bookshelf.models import Book

# Retrieve the book to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion
Book.objects.all()
# Output: <QuerySet []>
