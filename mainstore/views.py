from django.contrib.auth import get_user_model
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from mainstore.models import Book, UserBookRelation
from mainstore.permissions import IsOwnerOrAdminOrReadOnly
from mainstore.serializers import BooksSerializer, UserBookRelationSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

User = get_user_model()
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['price']
    search_fields = ['name', 'author_book']
    ordering_fields = ['price', 'author_book']

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()

    def list(self, request):
         serializer_class = UserSerializer(self.queryset, many=True)
         return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
         User= get_object_or_404(self.queryset, pk=pk)
         serializer_class =UserSerializer(User)
         return Response(serializer_class.data)

#


class UserBooksRelationView(mixins.UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserBookRelation.objects.all()
    serializer_class = UserBookRelationSerializer
    lookup_field = 'book'

    def get_object(self):
        obj, _ = UserBookRelation.objects.get_or_create(user=self.request.user, book_id=self.kwargs['book'])

        return obj

