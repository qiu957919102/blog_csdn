from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from repository import models
from utils.utilsfile import create_validate_code
from io import BytesIO
from django.core import serializers
# Create your views here.
from utils.auth import check_login
from backend.forms.account import LoginForm
from backend.forms.account import RegisterForm
import json
# def user_register(request):
#     """
#     注册方法
#     :param request:
#     :return:
#     """
#     if request.method == "GET":
#         return render(request, "user_register.html")
#     if request.method == "POST":
#         result = {'status': False, 'message': None, 'data': None}
#         CheckCode = request.session.get("CheckCode",None)
#         username = request.POST.get("username")
#         password1 = request.POST.get("password1")
#         password2 = request.POST.get("password2")
#         code_ver = request.POST.get("code_ver")
#         nickname = request.POST.get("nickname")
#         email = request.POST.get("email")
#         if all([username, password1, password2, nickname,CheckCode]):
#             if CheckCode.upper() == code_ver.upper():
#                 if password1 == password2:
#                     #models.UserInfo.objects.create(username=str(username),password=str(password1),email=email,nickname=str(nickname))
#                     # print(reset)
#                         ret = models.UserInfo.objects.filter(username=username)
#                         eret = models.UserInfo.objects.filter(email=email)
#                         if ret:
#                             result['message'] = "用户名🕐已被注册"
#                         elif eret:
#                             result['message'] = "邮箱已被注册"
#                         else:
#                             models.UserInfo.objects.create(username=username,password=password1,email=email,nickname=nickname)
#                             result['status'] = True
#
#                 else:
#                     result['message'] = '密码不一致'
#             else:
#                 result['message'] = '验证码错误'
#         else:
#             result['message'] = '请填写完毕注册信息'
#
#
#         # print(request.POST)
#         # print(request.POST.get("username"))
#         # print(request.POST.get("password1"))
#         # print(request.POST.get("password2"))
#         # print(request.POST.get("code_ver"))
#         # print(request.POST.get("email"))
#     return redirect('user_login.html')
#     # return render(request,"user_register.html")


def user_register(request):
    """
    注册方法
    :param request:
    :return:
    """

    if request.method == "GET":
        form_obj = RegisterForm(request=request)
        return render(request, "user_register.html",{"form_obj":form_obj})
    if request.method == "POST":
        """
        这个方法地配合ajax使用
        # result = {'status': False, 'message': None, 'data': None}
        """
        # result = {'status': False}
        form_obj = RegisterForm(request=request, data=request.POST)
        if form_obj.is_valid():
            # print(form_obj.cleaned_data)
            models.UserInfo.objects.create(
                username=form_obj.cleaned_data.get('username'),
                password=form_obj.cleaned_data.get('password1'),
                nickname=form_obj.cleaned_data.get('nickname'),
                email=form_obj.cleaned_data.get('email'),
            )
            return redirect('/user_register_success.html')
            # print(form_obj.cleaned_data.get('username'))
            # username = form.cleaned_data.get("username")
            # password1 = form.cleaned_data.get("password1")
            # nickname = form.cleaned_data.get("nickname")
            # email = form.cleaned_data.get("email")
            # print(username,password1,nickname,email)
            # return HttpResponse("....")
        else:
            """
            <ul class="errorlist"><li>username<ul class="errorlist"><li>用户名不能为空.</li></ul></li><li>password1<ul class="errorlist"><li>密码不能为空.</li></ul></li><li>password2<ul class="errorlist"><li>确认密码不能为空.</li></ul></li><li>check_code<ul class="errorlist"><li>验证码不能为空.</li></ul></li><li>nickname<ul class="errorlist"><li>昵称不能为空.</li></ul></li><li>email<ul class="errorlist"><li>验证码不能为空.</li></ul></li></ul>
            <ul class="errorlist"><li>check_code<ul class="errorlist"><li>验证码错误</li></ul></li><li>email<ul class="errorlist"><li>邮箱格式错误</li></ul></li><li>__all__<ul class="errorlist nonfield"><li>密码输入不一致</li></ul></li></ul>

            
            """
            """
            这个方法地配合ajax使用
                        # print(form_obj.errors.as_json())
            """
            # if 'check_code' in form.errors:
            #     result['message'] = '验证码错误或者过期'
            # else:
            #     result['message'] = '用户名或密码错误'
            # print(form_obj.errors)

            return render(request,'user_register.html',{"form_obj":form_obj})

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
        form_obj = LoginForm(request=request)
        return render(request, 'user_login.html',{"form_obj":form_obj})
    elif request.method == 'POST':
        result = {'status': False, 'message': None, 'data': None}
        form_obj = LoginForm(request=request, data=request.POST)
        if form_obj.is_valid():
            username = form_obj.cleaned_data.get('username')
            password = form_obj.cleaned_data.get('password')
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
                if form_obj.cleaned_data.get('rmb'):
                    request.session.set_expiry(60 * 60 * 24 * 30)
                return HttpResponse(json.dumps(result))
        else:
            # print(form.errors)
            # if 'check_code' in form.errors:
            #     result['message'] = '验证码错误或者过期'
            # else:
            #     result['message'] = '用户名或密码错误'
        # print(request.session.get('user_info'))
        # return HttpResponse(json.dumps(result))
            """
            {'username': [ValidationError(['用户名不能为空.'])], 'password': [ValidationError(['密码不能为空.'])], 'check_code': [ValidationError(['验证码不能为空.'])]}
            """
            # print(form_obj.errors.as_data())
            #
            # print(form_obj.errors.get("username"))
            # return render(request, 'user_login.html', {"form_obj": form_obj})
            return HttpResponse(form_obj.errors.as_json())



@check_login
def admin_index(request):
    # print(request.session.values())
    # print(request.session.get('user_info'))
    return render(request,"admin_index.html")



def logout(request):
    """
    注销
    :param request:
    :return:
    """
    """
    　request.session.clear() #清空(注销的时候使用)
    """
    request.session.clear()

    """
        # 1. 将session中的用户名、昵称删除
    request.session.flush()
    """
    return redirect('user_login.html')

@check_login
def user_register_success(request):
    # print(request.session.get('userinfo'))
    return render(request,'user_register_success.html')