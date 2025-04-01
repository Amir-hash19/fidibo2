from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import TemplateView



class BookView(TemplateView):
    template_name = "book.html"


