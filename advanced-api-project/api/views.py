from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# -----------------------------------------------------------
# ListView: Retrieve all books
# -----------------------------------------------------------
class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    Public endpoint that lists all books.
    Using ListAPIView provides built-in pagination, filtering, and optimization.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public access


# -----------------------------------------------------------
# DetailView: Retrieve a single book by ID
# -----------------------------------------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<id>/
    Public endpoint that retrieves a specific book.
    Uses RetrieveAPIView for optimized object lookup with pk.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# -----------------------------------------------------------
# CreateView: Add a new book
# -----------------------------------------------------------
class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Only authenticated users can create new books.
    perform_create() is overridden to add custom logic if needed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom behavior on creation.
        You can log actions, attach user data, or enforce rules here.
        """
        serializer.save()  # save the new Book instance


# -----------------------------------------------------------
# UpdateView: Modify an existing book
# -----------------------------------------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /api/books/<id>/update/
    Only authenticated users can update books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Custom update logic goes here.
        Automatically validates using serializer validation rules.
        """
        serializer.save()


# -----------------------------------------------------------
# DeleteView: Remove a book
# -----------------------------------------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/<id>/delete/
    Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
