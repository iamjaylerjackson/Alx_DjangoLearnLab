from relationship_app.models import Author, Book, Library, Librarian

# --- Query all books by a specific author ---
author_name = "Chimamanda Ngozi Adichie"  # Example
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)  # REQUIRED

print(f"Books by {author.name}:")
for book in books_by_author:
    print(f"- {book.title}")

# --- List all books in a specific library ---
library_name = "Accra Central Library"  # Example
library = Library.objects.get(name=library_name)  # REQUIRED
books_in_library = library.books.all()

print(f"\nBooks in {library.name}:")
for book in books_in_library:
    print(f"- {book.title} by {book.author.name}")

# --- Retrieve the librarian for a specific library ---
librarian = Librarian.objects.get(library=library)  # REQUIRED

print(f"\nLibrarian for {library.name}: {librarian.name}")
