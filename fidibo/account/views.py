from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from account.models import UserAccount
from django.views.generic import TemplateView, DetailView
from django.views.decorators.csrf import csrf_exempt
import json
import os


def home_view(request):
    return HttpResponse("this is home page!")
 



@csrf_exempt
def register_user(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")  
        age = int(request.POST.get("age", 0))  
        avatar = request.FILES.get("avatar")  

        user_created = UserAccount.objects.create(
            full_name=full_name,
            email=email,
            phone_number=phone_number,  
            age=age,
            avatar=avatar
        )
        return HttpResponse(f"The User with ID {user_created.id} created Successfully!")

    return HttpResponse("Invalid request method.", status=400)







