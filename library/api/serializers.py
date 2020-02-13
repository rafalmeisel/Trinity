from rest_framework import serializers

from library.api.models import Book, User


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'author', 'year', 'amount']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'login', 'name', 'privileges']
