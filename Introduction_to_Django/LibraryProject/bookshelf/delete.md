from bookshelf.models import Book
Book.objects.get(title="Nineteen Eighty-Four").delete
<!-- <bound method Model.delete of <Book: Book object (1)>> -->