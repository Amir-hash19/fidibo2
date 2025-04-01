from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from .serializers import BookSerializer
from .models import Book



class BookView(TemplateView):
    template_name = "book.html"


@api_view(["GET"])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)




