from rest_framework import generics, filters
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Add ordering support
    filter_backends = [filters.OrderingFilter]

    # Optional: specify fields you want to allow ordering by
    ordering_fields = ['title', 'author']

    # Optional default ordering
    ordering = ['title']
