from django.test import TestCase

from mainstore.models import Book
from mainstore.serializers import BooksSerializer


class LotSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Test Lot1', price=1111,  author_book='Author 1')
        book_2 = Book.objects.create(name='Test Lot2', price=2222,  author_book='Author 2')
        data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test Lot1',
                'price': '1111.00',
                'author_book': 'Author 1'
            },
            {
                'id': book_2.id,
                'name': 'Test Lot2',
                'price': '2222.00',
                'author_book': 'Author 2'
            },
        ]
        self.assertEqual(expected_data, data)
