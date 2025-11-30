from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer


# -----------------------------------------------------------
# ListView: Retrieve all books with filtering, searching, ordering
# -----------------------------------------------------------
class BookListView(generics.ListAPIView):
    """
    GET /api/books/

    Supports:
    - Filtering: ?title=xyz&author=John
    - Searching: ?search=something
    - Ordering: ?ordering=title or ?ordering=-publication_year
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Step 1: Filtering fields
    filterset_fields = ["title", "author", "publication_year"]

    # Step 2: Searching fields
    search_fields = ["title", "author"]

    # Step 3: Ordering fields
    ordering_fields = ["title", "publication_year"]
    ordering = ["title"]  # default ordering


# -----------------------------------------------------------
# DetailView: Retrieve one book
# -----------------------------------------------------------
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# -----------------------------------------------------------
# CreateView
# -----------------------------------------------------------
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


# -----------------------------------------------------------
# UpdateView
# -----------------------------------------------------------
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


# -----------------------------------------------------------
# DeleteView
# -----------------------------------------------------------
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
