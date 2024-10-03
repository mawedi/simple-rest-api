from rest_framework.serializers import ModelSerializer

from .models import Book

# serializer for the book
class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "name", "description"]