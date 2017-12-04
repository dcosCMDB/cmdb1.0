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

def searchhost(request):
    findall=dcos_host.objects.all()
    hostlist=[]
    for item in findall:
    	hostlist.append({"hostip":item.host_ip,"hostname":item.host_name,"env":item.env,"cpu":item.cpu,"mem":item.mem,"filesys":item.filesys})
    host_res = {"hostlist": hostlist}
    return HttpResponse(json.dumps(host_res), content_type='application/json')
