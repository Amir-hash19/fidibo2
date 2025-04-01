from django.urls import path
from book.views import BookView, book_list, create_book, display_book, delete_book

urlpatterns = [
    path("", BookView.as_view(), name="book-page"),
    path("api/book", book_list, name="book-list"),
    path("create-book/", create_book, name="create-book"),
    path("display-book/<int:book_id>", display_book, name="display-book"),
    path("delete-book/<int:book_id>", delete_book , name="delete-book"),
]
