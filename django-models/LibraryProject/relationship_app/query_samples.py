from . import models

b_by_author = models.Book.author_set.all()

b_in_lib = models.Library.books_set.all()

libn_for_lib = models.Librarian.library_set.all()