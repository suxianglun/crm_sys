#!/usr/bin/evn python
# -*- coding:utf-8 -*-
# @Date    : 2020-01-19
# @Author  : suxianglun
# @Describe :
# @Version :
from django import forms

from crm.form.baseform import BaseModeForm
from crm.models import Clue


class ClueForm(BaseModeForm):
    model = Clue
    fields = "__all__"
    widget = {
        'title': forms.TextInput(attrs={'placeholder': '线索'}),
        'phone': forms.NumberInput(attrs={'placeholder': '手机号'}, min_length=11, ),
    }
    error_message = {
        'title': {
            'required': '线索名称不能为空',
            # 'invalid': '格式错误',
            # 'min_length': '用户名最短8位',
        },
        'phone': {
            'required': '线索名称不能为空',
            'invalid': '格式错误',
            'min_length': '用户名最短11位',
        }
    }
