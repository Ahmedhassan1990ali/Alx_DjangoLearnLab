Book.objects.get(pk=1)
# <Book: Book object (1)>

Book.objects.get(pk=1).__dict__
# {'_state': <django.db.models.base.ModelState object at 0x0000021962790510>, 'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}