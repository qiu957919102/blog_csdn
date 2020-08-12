from django.shortcuts import render
from django.shortcuts import HttpResponse
from repository import models
from utils.utilsfile import create_validate_code
from io import BytesIO
# Create your views here.


def user_register(request):
    return render(request,"user_register.html")


def check_code(request):
    stream = BytesIO()
    print(stream)
    img, code = create_validate_code()
    print(img,code)
    img.save(stream, 'PNG')

    request.session['CheckCode'] = code
    return HttpResponse(stream.getvalue())