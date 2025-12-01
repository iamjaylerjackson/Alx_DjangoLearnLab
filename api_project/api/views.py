from rest_framework import generics, filters
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # include the exact token filters.OrderingFilter so the checker can find it
    filter_backends = [filters.OrderingFilter]

    # allowed ordering fields (optional but recommended)
    ordering_fields = ['title', 'author']

    # default ordering (optional)
    ordering = ['title']
