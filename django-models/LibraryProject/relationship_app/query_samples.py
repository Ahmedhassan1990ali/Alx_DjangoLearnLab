from . import models

b= models.Book.objects.get(pk=1)
b_by_author = b.author_set.all()


l = models.Library.objects.get(pk=1)
b_in_lib = l.books_set.all()


lib = models.Librarian.objects.get(pk=1)
libn_for_lib = lib.library_set.all()