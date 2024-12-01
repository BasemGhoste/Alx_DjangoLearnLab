from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete
<!-- <bound method Model.delete of <Book: Book object (1)>> -->