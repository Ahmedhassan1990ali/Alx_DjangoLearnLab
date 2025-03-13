from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Book, Author

class BookTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='testuser', password='testpass')
        self.author1= Author.objects.create(name="aaaa")
        self.author2= Author.objects.create(name="cccc")
        Book.objects.create(title="aa",publication_year=2000,author=self.author1)
        self.client= Client()
        self.client.login(username="testuser", password="testpass") 


    def test_Create_book(self):
        data = {"title": "cc", "author": self.author2.id, "publication_year": 2020}
        response = self.client.post("/api/books/create/", data)
        print(response.status_code)
        self.assertEqual(response.status_code,201)

    def test_Update_book(self):
        data = {"title": "cc", "author": self.author2.id, "publication_year": 2020}
        book_id = Book.objects.get(title="aa").id
        response = self.client.put(f"/api/books/update/{book_id}/", data,content_type="application/json")
        print(response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_Delete_book(self):
        book_id = Book.objects.get(title="aa").id
        response = self.client.delete(f"/api/books/delete/{book_id}/")
        print(response.status_code)
        self.assertEqual(response.status_code, 204)