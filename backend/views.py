from django.shortcuts import render
from django.shortcuts import HttpResponse
from repository import models
from utils.utilsfile import create_validate_code
from io import BytesIO
# Create your views here.


def user_register(request):
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get("username"))
        print(request.POST.get("password1"))
        print(request.POST.get("password2"))
        print(request.POST.get("code_ver"))
        print(request.POST.get("email"))
    return render(request,"user_register.html")


def check_code(request):
    stream = BytesIO()
    # print(stream)
    img, code = create_validate_code()
    # print(img,code)
    img.save(stream, 'PNG')

    request.session['CheckCode'] = code
    return HttpResponse(stream.getvalue())

def user_login(request):
    return render(request,"user_login.html")