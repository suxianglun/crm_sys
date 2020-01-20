#!/usr/bin/evn python
# -*- coding:utf-8 -*-
# @Date    : 2020-01-16
# @Author  : suxianglun
# @Describe :
# @Version :
from django.shortcuts import render, redirect, reverse

# Create your views here.
from django.views import View


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'index.html')
        else:
            # 反向解析并记住登录前的页面
            # url = reverse('login', kwargs={'next': request.path})
            url = reverse('login')
            return redirect(url)
