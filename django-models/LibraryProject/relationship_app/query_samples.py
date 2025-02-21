from . import models


author = ""
a = models.Author.objects.get(name=author)
result = a.books.all()

library_name = ""
l = models.Library.objects.get(name=library_name)
result = l.books.all()

librarian = l.librarian.get()