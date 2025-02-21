from . import models


book_title = "b"
b= models.Book.objects.get(title=book_title)
b_by_author = b.author.all()

library_name = "a"
l = models.Library.objects.get(name=library_name)
b_in_lib = l.books.all()

librarian_name = "s"
lib = models.Librarian.objects.get(name=librarian_name)
libn_for_lib = lib.library.all()