#!/usr/bin/evn python
# -*- coding:utf-8 -*-
# @Date    : 2019-12-09
# @Author  : suxianglun
# @Describe :
# @Version : 
from django.forms import ModelForm


class BaseModeForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(BaseModeForm, self).__init__(*args, **kwargs)
        for k, v in self.fields.item():
            v.widget.attr['attr'] = 'form-control'
