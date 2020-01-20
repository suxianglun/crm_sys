#!/usr/bin/evn python
# -*- coding:utf-8 -*-
# @Date    : 2020-01-17
# @Author  : suxianglun
# @Describe :
# @Version :
from django.views import View
from django.shortcuts import render, redirect
from crm import models


class ClueList(View):
    def get(self, request):
        clue_list = models.Clue.objects.all()
        return render(request, 'clue_list.html', {'clue_list': clue_list})
