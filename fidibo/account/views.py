from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from account.models import UserAccount
from django.views.generic import TemplateView, DetailView
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
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



@csrf_exempt
def delete_user(request, user_id):
    try:
        user_id = UserAccount.objects.get(id=user_id)
        user_id.delete()
        return HttpResponse(f"The user with was deleted successfully")
    except UserAccount.DoesNotExist:
        HttpResponse(f"The user with {user_id.id} ID does not existed!")    
    
    

@csrf_exempt
def display_user(request, user_id):
    try:
        user = UserAccount.objects.get(id=user_id)
        user_data = {
            "id":user.id,
            "full_name":user.full_name,
            "email":user.email,
            "avatar":user.avatar.url if user.avatar else None,
            "age":user.age
        }
        return JsonResponse(user_data)
    except UserAccount.DoesNotExist:
        return JsonResponse({"error":"User not found"} ,status=404)
    



@csrf_exempt
def edit_user(request, user_id):
    try:
        user = UserAccount.objects.get(id=user_id)
    except UserAccount.DoesNotExist:
        return JsonResponse({"error":"User not found"}, status=404)

    if request.method in ["PATCH", "PUT"]:
        data = json.loads(request.body.decode("utf-8")) if request.body else {}
        if request.method == "PUT":
            user.full_name = data.get("full_name", user.full_name)
            user.email = data.get("email", user.email)
            user.phone_number = data.get("phone_number", user.phone_number)
            user.age = data.get("age", user.age)
            if "avatar" in request.FILES:
                user.avatar = request.FIELS["avatar"]


        elif request.method == "PATCH":
            if "full_name" in data:
                user.full_name = data["full_name"]
            if "email" in data:
                user.email = data["email"]
            if "phone_number" in data:
                user.phone_number = data["phone_number"]
            if "age" in data:
                user.age = data ["age"]
            if "avatar" in request.FILES:
                user.avatar = request.FIELS["avatar"]     
        user.save()
        return HttpResponse("The User Updated Successfully!")
                    






