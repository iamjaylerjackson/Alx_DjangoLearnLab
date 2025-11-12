from relationship_app.models import Author, Book, Library

# Get all authors
all_authors = Author.objects.all()

# Get all books
all_books = Book.objects.all()

# Get all libraries
all_libraries = Library.objects.all()

# Get books by a specific author
author = Author.objects.get(name="Chimamanda Ngozi Adichie")  # example name
books_by_author = Book.objects.filter(author=author)  # ← this is the required line

# Get all books published after 2020
recent_books = Book.objects.filter(publication_year__gt=2020)

# Get all books in a specific library
library = Library.objects.get(name="Accra Central Library")
books_in_library = library.books.all()

# Print results to verify (optional)
print("Books by", author.name, ":", books_by_author)
print("Recent Books:", recent_books)
print("Books in", library.name, ":", books_in_library)
