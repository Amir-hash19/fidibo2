from django.urls import path
from book.views import BookView 

urlpatterns = [
    path("", BookView.as_view(), name="book-page"),
]
