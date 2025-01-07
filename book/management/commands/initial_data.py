from book.models import BookModel
from auth.models import UserModel
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.conf import settings


class Command(BaseCommand):
    help = 'Espera a que MongoDB esté disponible'

    def handle(self, *args, **kwargs):
        self.stdout.write('Insert data inital in MongoDB...')
        user_model = UserModel()
        user_data = {
            "username": settings.TEST_USERNAME,
            "password": settings.TEST_PASSWORD,
            "first_name": "test_first_name",
            "last_name": "test_last_name"
        }
        user_model.delete_many({})
        user_model.create_user(
            user_data["username"],
            make_password(user_data["password"]),
            **{
                "first_name": user_data["first_name"],
                "last_name": user_data["last_name"]
            }
        )
        book_model = BookModel()
        books_data = [
            {
                "title": "Clean Code",
                "author": "Robert C. Martin",
                "genre": "Ficción",
                "published_date": "2024-01-01",
                "price": 39.99,
            },
            {
                "title": "The Pragmatic Programmer",
                "author": "Andrew Hunt",
                "genre": "Ficción",
                "published_date": "2024-02-02",
                "price": 29.99,
            },
            {
                "title": "Design Patterns",
                "author": "Erich Gamma",
                "genre": "Ficción",
                "published_date": "2024-03-03",
                "price": 49.99,
            },
            {
                "title": "Refactoring",
                "author": "Martin Fowler",
                "genre": "Ficción",
                "published_date": "2024-04-04",
                "price": 45.00,
            },
            {
                "title": "You Don't Know JS",
                "author": "Kyle Simpson",
                "genre": "Ficción",
                "published_date": "2024-05-05",
                "price": 19.99,
            }
        ]

        book_model.delete_many({})
        book_model.insert_many(books_data)
        self.stdout.write(self.style.SUCCESS('¡Seed books in MongoDB!'))
