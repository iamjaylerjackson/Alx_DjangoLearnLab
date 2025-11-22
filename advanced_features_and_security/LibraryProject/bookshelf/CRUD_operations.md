---

## 📘 **File: `CRUD_operations.md`**
```markdown
# CRUD Operations Summary

This file summarizes all Create, Retrieve, Update, and Delete operations performed on the Book model.

---

## 🟩 Create

```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book
# Output: <Book: 1984 by George Orwell (1949)>
```
