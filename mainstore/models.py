from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Book(models.Model):
    name = models.CharField(max_length=124)
    author_book = models.CharField(max_length=124, default='author Book')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='my_books')
    readers = models.ManyToManyField(User, through='UserBookRelation',related_name='my_like_books')


    def __str__(self):
        return f'Name of Book: {self.name} | Author: {self.author_book}'

class UserBookRelation(models.Model):
    RATE_CHOICES = (
        (1, 'Ok'),
        (2, 'Fine'),
        (3, 'Good'),
        (4, 'Amazing'),
        (5, 'Incredible')
    )


    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)


    def __str__(self):
        return f'{self.user.username}: {self.book.name}, Rate: {self.rate}'
