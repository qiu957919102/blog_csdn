#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.core.exceptions import ValidationError
from django import forms as django_forms
from django.forms import fields as django_fields
from django.forms import widgets as django_widgets

from repository import models

from .base import BaseForm


class LoginForm(BaseForm, django_forms.Form):
    # username = django_fields.CharField(
    # min_length=6,
    # max_length=20,
    #     error_messages={'required': '用户名不能为空.', 'min_length': "用户名长度不能小于6个字符", 'max_length': "用户名长度不能大于32个字符"}
    # )
    username = django_fields.CharField()

    # password = django_fields.RegexField(
    #     '^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$\%\^\&\*\(\)])[0-9a-zA-Z!@#$\%\^\&\*\(\)]{8,32}$',
    #     min_length=12,
    #     max_length=32,
    #     error_messages={'required': '密码不能为空.',
    #                     'invalid': '密码必须包含数字，字母、特殊字符',
    #                     'min_length': "密码长度不能小于8个字符",
    #                     'max_length': "密码长度不能大于32个字符"}
    # )
    password = django_fields.CharField()
    rmb = django_fields.IntegerField(required=False)

    check_code = django_fields.CharField(
        error_messages={'required': '验证码不能为空.'}
    )

    def clean_check_code(self):
        if self.request.session.get('CheckCode').upper() != self.request.POST.get('check_code').upper():
            raise ValidationError(message='验证码错误', code='invalid')


class RegisterForm(BaseForm, django_forms.Form):
    username = django_fields.CharField(
        error_messages={'required': '用户名不能为空.'}
    )
    """
    # 定义为密码文本,render_value设置为验证不通过时不把密码刷新掉
    """
    password1 = django_fields.CharField(
        error_messages={'required': '密码不能为空.'}
    )
    password2 = django_fields.CharField(
        error_messages={'required': '确认密码不能为空.'}
    )
    check_code = django_fields.CharField(
        error_messages={'required': '验证码不能为空.'}
    )
    nickname = django_fields.CharField(
        error_messages={'required': '昵称不能为空.'}
    )
    email = django_fields.EmailField(
        error_messages={'required': '验证码不能为空.','invalid': '邮箱格式错误'}
    )

    def clean(self):
        v1 = self.cleaned_data.get('password1')
        v2 = self.cleaned_data.get('password2')
        print(v1,v2)
        if v1 == v2:
            pass
        else:
            from django.core.exceptions import ValidationError,NON_FIELD_ERRORS
            raise ValidationError('密码输入不一致')


    def clean_check_code(self):
        if self.request.session.get('CheckCode').upper() != self.request.POST.get('check_code').upper():
            raise ValidationError(message='验证码错误', code='invalid')

"""


from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': '请输入用户名'}))
    first_name = forms.CharField(widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': '请输入名字'}))
    last_name = forms.CharField(widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': '请输入姓氏'}))
    password = forms.CharField(widget=forms.PasswordInput({
        'class': 'form-control',
        'placeholder': '请输入密码'}))
    email = forms.CharField(widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': '请输入邮箱'}))

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password')

"""


