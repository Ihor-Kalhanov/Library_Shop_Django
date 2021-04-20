from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from mainstore.models import Book, UserBookRelation

User = get_user_model()
class BooksSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(ModelSerializer): # new

    class Meta:
        model = User
        fields = ('id', 'username','first_name', 'email')

class UserBookRelationSerializer(ModelSerializer):
    class Meta:
        model = UserBookRelation
        fields = ('book', 'like', 'in_bookmarks', 'rate')