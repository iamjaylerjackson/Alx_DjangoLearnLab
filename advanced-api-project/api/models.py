from django.db import models

# Author model to store information about book authors


class Author(models.Model):
    name = models.CharField(max_length=100)  # Author's name

    def __str__(self):
        return self.name

# Book model to store information about books


class Book(models.Model):
    title = models.CharField(max_length=200)             # Book title
    publication_year = models.IntegerField()             # Year book was published
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE)  # Relationship to Author

    def __str__(self):
        return self.title
