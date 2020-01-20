#!/usr/bin/evn python
# -*- coding:utf-8 -*-
# @Date    : 2019-11-21
# @Author  : suxianglun
# @Describe :
# @Version :
from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User

class RegisterForm(UserCreationForm):
    '''
        Django的内置了一个用户注册表单：django.contrib.auth.forms.UserCreationForm，
        不过这个表单的一个小问题是它关联的是 django 内置的 User 模型，我们要继承这个类
        然后重写Meta
        '''

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '用户名'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码'}),
        }
