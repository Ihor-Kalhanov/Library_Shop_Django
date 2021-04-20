from django.contrib import admin

from mainstore.models import Book, UserBookRelation

admin.site.register(Book)
admin.site.register(UserBookRelation)
