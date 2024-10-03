from django.shortcuts import render

from .models import Book
from .serializer import BookSerializer

from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ListBooksAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class RetrieveBookAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id", "")

        try:
            # Retrieving a book from the database
            book = Book.objects.get(id=id)

            # serialization process
            serializer = BookSerializer(book)
        
        except Book.DoesNotExist:
            return Response({"message": "This book is not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception:
            return Response({"message": "Server Error!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

        return Response(serializer.data, status=status.HTTP_200_OK)


class RegisterBookAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteBookAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UpdateBookAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
