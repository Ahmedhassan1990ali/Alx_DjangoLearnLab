from . import models


author_name = ""
a = models.Author.objects.get(name=author_name)
result = a.books.all()
result = models.Book.objects.filter(author__name=author_name)

library_name = ""
l = models.Library.objects.get(name=library_name)
result = l.books.all()

librarian = l.librarian.get()
librarian = models.Library.objects.filter(library__name=library_name)