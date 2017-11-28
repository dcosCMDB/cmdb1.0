# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import json
from CMDBpro.models import dcos_host

def showhost(request):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        response = HttpResponseRedirect('/showhost')
        return render(request, 'hosttable.html')
    else:
        response = HttpResponseRedirect('/')
        return render(request, 'login.html')
