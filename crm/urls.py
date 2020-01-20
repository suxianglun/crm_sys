#!/usr/bin/evn python
# -*- coding:utf-8 -*-
# @Date    : 2019-11-13
# @Author  : suxianglun
# @Describe :
# @Version : 
from django.urls import path, re_path,include
from crm.views import home
import user
urlpatterns = [
    # path('login/', views.LoginView.as_view(), name='login'),
    re_path(r'^.*$', home.HomeView.as_view(), name='index'),
]

# 增加的条目
# handler400 = views.bad_request
# handler403 = views.permission_denied
# handler404 = views.page_not_found
# handler500 = views.error