from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from account.models import UserAccount
from .serializers import BookSerializer
from .models import Book
import json



class BookView(TemplateView):
    template_name = "book.html"


@api_view(["GET"])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)






@csrf_exempt
def create_book(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            # دریافت اطلاعات نویسنده از داده‌های ورودی
            author_id = data.get("author_id")  # فرض کنید کلید author_id در داده‌های ورودی موجود باشد
            if not author_id:
                return JsonResponse({"error": "Author ID is required"}, status=400)

          
            try:
                author = UserAccount.objects.get(id=author_id)
            except UserAccount.DoesNotExist:
                return JsonResponse({"error": "Author not found"}, status=404)

            # ایجاد کتاب جدید
            created_book = Book.objects.create(
                title=data.get("title"),
                slug=data.get("slug"),
                description=data.get("description"),
                price=data.get("price"),
                status=data.get("status"),
                author=author  
            )

            return JsonResponse({"message": "The book was created successfully!", "book_id": created_book.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)




@csrf_exempt
def display_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        author_data = {
            "id":book.author.id,
            "full_name":book.author.full_name,
            "email":book.author.email
        }


        book_data = {
            "id":book.id,
            "title":book.title,
            "slug":book.slug,
            "description":book.description,
            "price":book.price,
            "author":author_data,
            "status":book.status,
        }
        return JsonResponse({"book_data":book_data})
    except UserAccount.DoesNotExist:
        return JsonResponse({"error":"User not found"} ,status=404)