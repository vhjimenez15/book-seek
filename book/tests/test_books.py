from django.urls import reverse
from unittest import TestCase
from rest_framework import status
from urllib.parse import urlencode
from config.client import CustomAPIClient
from django.conf import settings


class BookAPITestCase(TestCase):

    def setUp(self):
        self.valid_book = {
            "title": "El viejo y el mar",
            "author": "Ernest Heminqway",
            "published_date": "2024-06-06",
            "genre": "Ficción",
            "price": 20
        }

        self.client = CustomAPIClient()
        self.client.set_auth_token(self.get_token())

    def get_token(self):
        """Obtains a JWT token for authentication."""
        user_data = {
            "username": settings.TEST_USERNAME,
            "password": settings.TEST_PASSWORD
        }
        response = self.client.post(reverse('login'), user_data)
        return response.json()['access']

    def test_create_book(self):
        """Test creating a book."""
        book_create_url = reverse('book-list')
        response = self.client.post(
            book_create_url,
            self.valid_book,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.book_id = response.data["id"]

    def test_list_books(self):
        """Test to list books."""
        book_list_url = reverse('book-list')
        response = self.client.get(book_list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_list_one_book(self):
        """Test to list a book."""
        self.test_create_book()
        book_list_url = reverse('book-list')
        query_params = {'book_id': self.book_id}
        full_url = f"{book_list_url}?{urlencode(query_params)}"
        response = self.client.get(
            full_url,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.book_id)

    def test_update_book(self):
        """Test to update a book."""
        self.test_create_book()
        book_update_url = reverse("book-detail", args=[str(self.book_id)])
        updated_book = self.valid_book.copy()
        updated_book['title'] = 'Title updated'
        response = self.client.put(
            book_update_url,
            updated_book,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Title updated')

    def test_delete_book(self):
        """Try deleting a book."""
        self.test_create_book()
        book_delete_url = reverse("book-detail", args=[str(self.book_id)])
        response = self.client.delete(
            f"{book_delete_url}",
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
