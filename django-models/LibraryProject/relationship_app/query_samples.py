from . import models


author_name = ""
author = Author.objects.get(name=author_name)
result = models.Book.objects.filter(author=author)

library_name = ""
l = models.Library.objects.get(name=library_name)
result = l.books.all()

librarian = l.librarian.get()
librarian = models.Librarian.objects.filter(library=library_name)