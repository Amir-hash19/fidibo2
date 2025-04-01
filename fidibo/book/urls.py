from django.urls import path
from book.views import BookView, book_list

urlpatterns = [
    path("", BookView.as_view(), name="book-page"),
    path("api/book", book_list, name="book-list"),
]
