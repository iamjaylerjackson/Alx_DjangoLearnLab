from relationship_app.models import Author, Book, Library

# Get all authors
all_authors = Author.objects.all()

# Get all books
all_books = Book.objects.all()

# Get all libraries
all_libraries = Library.objects.all()

# Get books by a specific author
author_name = "Chimamanda Ngozi Adichie"  # Example name
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)  # ← REQUIRED line

# Get a specific library by name
library_name = "Accra Central Library"  # Example name
library = Library.objects.get(name=library_name)  # ← REQUIRED line

# Get all books in that library
books_in_library = library.books.all()

# Print results (optional)
print("Books by", author.name, ":", books_by_author)
print("Books in", library.name, ":", books_in_library)
