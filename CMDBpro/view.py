# -*- coding: utf-8 -*-
#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from CMDBpro.models import Loginuser

class UserForm(forms.Form): 
    username = forms.CharField(label='username',max_length=100)
    password = forms.CharField(label='password',widget=forms.PasswordInput())

def index(request):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        response = HttpResponseRedirect('/')
        return render(request, 'index.html')
    else:
        response = HttpResponseRedirect('/')
        return render(request, 'login.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = Loginuser.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/index')
                request.session['IS_LOGIN'] = True
                request.session['username'] = username
                return response
            else:
                #比较失败，还在login
                return render(request, 'login.html')
                
def logout(request):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        del request.session['IS_LOGIN']
        del request.session['username']
        return render(request, 'login.html')
    else:
        response = HttpResponseRedirect('/')
        return render(request, 'login.html')
