from django.shortcuts import render
from django.shortcuts import HttpResponse
from repository import models
from utils.utilsfile import create_validate_code
from io import BytesIO
# Create your views here.


def user_register(request):
    if request.method == "POST":
        result = {'status': False, 'message': None, 'data': None}
        CheckCode = request.session.get("CheckCode",None)
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        code_ver = request.POST.get("code_ver")
        nickname = request.POST.get("nickname")
        email = request.POST.get("email")
        if CheckCode.upper() == code_ver.upper():
            if password1 == password2:
                #models.UserInfo.objects.create(username=str(username),password=str(password1),email=email,nickname=str(nickname))
                # print(reset)
                if all([username,password1,password2,nickname]):
                    ret = models.UserInfo.objects.filter(username=username)
                    eret = models.UserInfo.objects.filter(email=email)
                    if ret:
                        result['message'] = "用户名🕐已被注册"
                    elif eret:
                        result['message'] = "邮箱已被注册"
                    else:
                        models.UserInfo.objects.create(username=username,password=password1,email=email,nickname=nickname)
                        result['status'] = True
                else:
                    result['message'] = '请填写完毕注册信息'
            else:
                result['message'] = '密码不一致'
        else:
            result['message'] = '验证码错误'


        # print(request.POST)
        # print(request.POST.get("username"))
        # print(request.POST.get("password1"))
        # print(request.POST.get("password2"))
        # print(request.POST.get("code_ver"))
        # print(request.POST.get("email"))
        return render(request,'user_login.html')
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