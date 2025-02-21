from . import models


author = ""
a = models.Author.objects.get(name=author)
result = a.books.all()

library = ""
l = models.Library.objects.get(name=library)
result = l.books.all()

librarian = l.librarian.get()