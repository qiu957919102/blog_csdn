from django.shortcuts import render
from repository import models
# Create your views here.


def user_register(request):
    return render(request,"user_register.html")