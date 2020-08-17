from django.shortcuts import render
from django.shortcuts import HttpResponse
from repository import models
from utils.utilsfile import create_validate_code
from io import BytesIO
from django.core import serializers
# Create your views here.
from utils.auth import check_login
from backend.forms.account import LoginForm
import json
def user_register(request):
    """
    注册方法
    :param request:
    :return:
    """
    if request.method == "POST":
        result = {'status': False, 'message': None, 'data': None}
        CheckCode = request.session.get("CheckCode",None)
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        code_ver = request.POST.get("code_ver")
        nickname = request.POST.get("nickname")
        email = request.POST.get("email")
        if all([username, password1, password2, nickname,CheckCode]):
            if CheckCode.upper() == code_ver.upper():
                if password1 == password2:
                    #models.UserInfo.objects.create(username=str(username),password=str(password1),email=email,nickname=str(nickname))
                    # print(reset)
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
                    result['message'] = '密码不一致'
            else:
                result['message'] = '验证码错误'
        else:
            result['message'] = '请填写完毕注册信息'


        # print(request.POST)
        # print(request.POST.get("username"))
        # print(request.POST.get("password1"))
        # print(request.POST.get("password2"))
        # print(request.POST.get("code_ver"))
        # print(request.POST.get("email"))
        return render(request,'user_login.html')
    return render(request,"user_register.html")


def check_code(request):
    """
    验证码方法
    :param request:
    :return:
    """
    stream = BytesIO()
    # print(stream)
    img, code = create_validate_code()
    # print(img,code)
    img.save(stream, 'PNG')

    request.session['CheckCode'] = code
    return HttpResponse(stream.getvalue())

# def user_login(request):
#     """
#     用户登录方法
#     :param request:
#     :return:
#     """
#     if request.method == 'GET':
#         return render(request, "user_login.html")
#     if request.method == 'POST':
#         result = {'status': False, 'message': None, 'data': None}
#         CheckCode = request.session.get("CheckCode",None)
#         username = request.POST.get("username")
#         password = request.POST.get("password1")
#         code_ver = request.POST.get("code_ver")
#         rmb = request.POST.get("rmb")
#         # print(request.POST)
#         if all([username, password, CheckCode]):
#             if CheckCode.upper() == code_ver.upper():
#                 user_info = models.UserInfo.objects.filter(username=username,password=password).only('nid', 'nickname','username', 'email','avatar',)
#                 # user_info = models.UserInfo.objects.filter(username=username,password=password).values('nid', 'nickname','username', 'email','avatar',)
#                 # print(user_info)
#
#                 if user_info:
#                     result['status'] = True
#                     user_info = serializers.serialize('json',user_info)
#                     # print(user_info)
#                     request.session['user_info'] = user_info
#                     if rmb:
#                         request.session.set_expiry(60 * 60 * 24 * 30)
#                     return render(request, "index.html")
#                 else:
#                     result['message'] = '用户名或者密码错误'
#             else:
#                 result['message'] = '验证码错误'
#         else:
#             result['message'] = '请填写完毕登录信息'

def user_login(request):
    """
    登陆
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'user_login.html')
    elif request.method == 'POST':
        result = {'status': False, 'message': None, 'data': None}
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user_info = models.UserInfo.objects. \
                filter(username=username, password=password). \
                values('nid', 'nickname',
                       'username', 'email',
                       'avatar',
                       'blog__nid',
                       'blog__site').first()
            print(user_info)
            if not user_info:
                # result['message'] = {'__all__': '用户名或密码错误'}
                result['message'] = '用户名或密码错误'
            else:
                result['status'] = True
                request.session['user_info'] = user_info
                if form.cleaned_data.get('rmb'):
                    request.session.set_expiry(60 * 60 * 24 * 30)
        else:
            print(form.errors)
            if 'check_code' in form.errors:
                result['message'] = '验证码错误或者过期'
            else:
                result['message'] = '用户名或密码错误'
        return HttpResponse(json.dumps(result))



@check_login
def admin_index(request):
    print(request.session.values())
    return render(request,"admin_index.html")