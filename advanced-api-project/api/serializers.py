from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# Serializer for Book model with custom validation


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation: publication year cannot be in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future.")
        return value

# Serializer for Author model, including nested books


class AuthorSerializer(serializers.ModelSerializer):
    # Nested BookSerializer to include all books for an author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
